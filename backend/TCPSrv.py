import sys, time, socket, select
import Cmd, ServerProcess

from scapy.all import *
import DB

Port = 8888

AliveSendEvery = 2    # Send alive every x seconds
LastAliveSent = -AliveSendEvery  # Make sure it fires immediatelly

########################################################################
## Init Socket

def SetSocketOptions(aSocket):
  aSocket.setblocking(False);
  aSocket.settimeout(0.5)
  aSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  aSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
  aSocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
  # It activates after 1 second (after_idle_sec) of idleness,
  # then sends a keepalive ping once every 1 seconds (interval_sec),
  # and closes the connection after 1 failed ping (max_fails)
  # aSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
  # aSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 1)
  # aSocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 1)
  return
  
# Listener socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
try:
  SetSocketOptions(Socket)
  # Bind socket to local host and port
  Socket.bind(('', Port))
  Socket.listen(socket.SOMAXCONN)
  
except socket.error as msg:
  print 'Server socket creation failed with error message (' + str(msg[0]) + '): ' + msg[1]
  print 'Server will now exit'
  Socket.close
  raise

print 'Server socket activated'

# List of socket clients, contains by default also the listener
ConnectionList = [Socket] 

########################################################################
## Socket line helper functions

def SocketConnected(aSocket):
  return aSocket in ConnectionList

#den douleuei kala  
def SocketDisconnect(aSocket):
  if SocketConnected(aSocket):
    try:
      ConnectionList.remove(aSocket)
      #socket disconnect - update table
      Delete_SubNode((aSocket.getpeername()[0]))
      aSocket.shutdown()  # Destroy connection
      aSocket.close()  # Destroy socket object
    except:
      pass

  return
  
def SocketIsReadable(aSocket):
  if not SocketConnected(aSocket):
    Result = False
  else:
    ReadableSockets, WritableSockets, ErrorSockets = select.select([aSocket], [], [], 0)
    Result = len(ReadableSockets) > 0

  return Result
  
def ReceiveBytes(aSocket, aNumBytes):
  Result = ""
  try:
    while len(Result) != aNumBytes:
      Received = aSocket.recv(aNumBytes - len(Result))
      if not Received:
        raise Exception("Socket disconnected while reading")
      Result = Result + Received
  except:
	SocketDisconnect(aSocket)
	raise
    
  return Result

def SendBytes(aSocket, aBuffer):
  try:
	aSocket.sendall(aBuffer)
  except:
	SocketDisconnect(aSocket)
	raise  
  return
  
########################################################################
## Command packing/unpacking
MaxPacketLengthCharacters = 6;
MaxCmdLengthCharacters = 3;

ctInitiator = "I"
ctResponse = "R"
ctResponseException = "E"
ciRequiresResponse = "Y"
ciRequiresNoResponse = "N"

def PadNum(aNum, aTotDigits):
  NumStr = str(aNum)
  
  return '0' * (aTotDigits - len(NumStr)) + NumStr

def PackCmd(aCmd, aData, aWaitResponse):

  Result = ctInitiator
  if aWaitResponse:
    Result = Result + ciRequiresResponse
  else:
    Result = Result + ciRequiresNoResponse

  CmdDataStr = PadNum(aCmd, MaxCmdLengthCharacters) + aData
  CmdDataStr = PadNum(len(CmdDataStr), MaxPacketLengthCharacters) + CmdDataStr

  Result = Result + CmdDataStr
  
  return Result

########################################################################
## Processing

def ExecCmd(aSocket, aCmd, aData, aWaitResponse = True, aTimeoutSec = None):

  Result = ""

  # Write the command
  SendBytes(aSocket, PackCmd(aCmd, aData, aWaitResponse))

  # Pick up response
  if aWaitResponse:
    StartTime = time.time()
    while True:
      if SocketIsReadable(aSocket):
        BufferType = ReceiveBytes(aSocket, 1)
        if BufferType == ctInitiator:
          ProcessInitiatorBuffer(aSocket)
        else:
          break  # continue the processing in ProcessResultBuffer
      if aTimeoutSec != None:
        if time.time() - StartTime >= aTimeoutSec:
          raise Exception("Timeout in ExecCmd")
    Result = ProcessResultBuffer(aSocket, BufferType)
     
  return Result

def ProcessInitiatorBuffer(aSocket):
	
  RequiresResponse = ReceiveBytes(aSocket, 1) == ciRequiresResponse
  ReadBuf = ReceiveBytes(aSocket, MaxPacketLengthCharacters)
  BytesInPacket = int(ReadBuf)
  CmdStr = ReceiveBytes(aSocket, MaxCmdLengthCharacters)
  ReadBuf = ReceiveBytes(aSocket, BytesInPacket - MaxCmdLengthCharacters)

  try:
    Result = ServerProcess.ProcessCommand (aSocket, int(CmdStr), ReadBuf)
    if RequiresResponse:
	  SendBytes(aSocket, ctResponse + PadNum(len(Result), MaxPacketLengthCharacters) + Result)
  except Error as Err:
    Result = Err
    if RequiresResponse:
      SendBytes(aSocket, ctResponseException + PadNum(len(Result), MaxPacketLengthCharacters) + Result)

  return

def ProcessResultBuffer(aSocket, aBufferType):
	
  Response = ReceiveBytes(aSocket, MaxPacketLengthCharacters)
  BytesInPacket = int(Response)
  Response = ReceiveBytes(aSocket, BytesInPacket)
    
  if aBufferType == ctResponseException:
    raise Exception(Response)

  return Response

# Insert subnode to subnode table
def Delete_SubNode(ip):
	try:
		DB.Cursor.execute("UPDATE subnode SET Status = 0, IP = NULL WHERE IP=%s",(ip))
		DB.Connection.commit()
		print('\x1b[6;31;40m' + "Client disconnected " + '\x1b[0m' + ip)
	except Error as error:
		print(error)
		
def updateIP_Status(mac,ip):
	try:
		DB.Cursor.execute("UPDATE subnode SET Status = 1,IP=%s WHERE MAC=%s ",(ip,mac))
		DB.Connection.commit()
	except Error as error:
		print(error)
		
def getMac(mac,ip):
	check=0
	#Select ip,id_sub and update Status to database
	row = DB.Cursor.execute("SELECT MAC,IP,Status FROM subnode WHERE MAC=%s",(mac))
	row = DB.Cursor.fetchone()
	if row:
		check=1
		IP = row[1]
		Status = row[2]
		if IP and Status:
			print "MAC exists"
		else:
			updateIP_Status(mac,ip)
			print "Ip and Status updated"
	else:
		check=0
	return check

def InsertMac(mac,ip):
	query = ("INSERT INTO subnode "
		"(MAC,IP,Status) " 
		"VALUES (%(MAC)s,%(IP)s,%(Status)s)")
	args = {
	'MAC': mac,
	'IP': ip,
	'Status': 1,
	}
	try:
		DB.Cursor.execute(query,args)
		DB.Connection.commit()
	except Error as error:
		print(error)
	
def checkConnectedDevices(ip):
	rangeIP=ip
	interface = "wlan0"
	try:
		alive,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=rangeIP),iface = interface, timeout=2, verbose=0)
		for i in range(0,len(alive)):
			mac = alive[i][1].hwsrc
			ip = alive[i][1].psrc
			if getMac(mac,ip) != 1:
				InsertMac(mac,ip)	
				print "Registered"		
	except:
		pass
		
		  
def SocketProcess():

  # Send keep alive to all lines
  global LastAliveSent

  # Check if it is time to send the keep alive message
  NowTime = time.time()
  if NowTime - LastAliveSent >= AliveSendEvery:
    try:
      for Sock in ConnectionList:
        if Sock != Socket:
          ExecCmd(Sock, Cmd.cmdAlive, "", False)
    except:
        pass
    LastAliveSent = NowTime

  # Get the list sockets which are ready to be read through select
  #print "Checking for reads"
  ReadSockets, WriteSockets, ErrorSockets = select.select(ConnectionList, [], [], 0)
  
  for Sock in ReadSockets:
    # New connection
    if Sock == Socket:
      # Handle the case in which there is a new connection received
      (NewSocket, (NewAddr, NewPort)) = Socket.accept()
      ConnectionList.append(NewSocket)
      SetSocketOptions(NewSocket)
      checkConnectedDevices(NewAddr)
      print "Client (%s) " % NewAddr + '\x1b[1;32;40m' + 'connected' + '\x1b[0m'
    else:
      # Check incoming messages from the peer
      while SocketConnected(Sock) and SocketIsReadable(Sock):
        try:
          BufferType = ReceiveBytes(Sock, 1)  # ctInitiator, ctResponse or ctResponseException
          if BufferType == ctInitiator:
			ProcessInitiatorBuffer(Sock)
          else:
	        # Discard buffer, we have a result that we have not asked for
		    # This should never happen
            ProcessResultBuffer(Sock, ctResponse)
        except:
          pass

  return
