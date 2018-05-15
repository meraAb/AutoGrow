import time, socket, select
import Cmd, ClientProcess, Tasks , HW

Host = "192.168.0.2"
#Host = "192.168.0.57"
Port = 8888

AliveSendEvery = 2    # Send alive every x seconds
DataSendEvery = 5	  # Send humidity value every 30 seconds
LastAliveSent = -AliveSendEvery  # Make sure it fires immediatelly
LastDataSent = -DataSendEvery    # Make sure it fires immediatelly

########################################################################
## Init Socket

SocketConnected = False
Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
Socket.setblocking(False)
Socket.settimeout(0.5)
Socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
Socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
# It activates after 1 second (after_idle_sec) of idleness,
# then sends a keepalive ping once every 1 seconds (interval_sec),
# and closes the connection after 1 failed ping (max_fails)
# Socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
# Socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 1)
# Socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 1)

########################################################################
## Socket line helper functions
def SetSocketConnectedInternal(aConnected):
  global SocketConnected
  
  if aConnected != SocketConnected:
    SocketConnected = aConnected
    #if SocketConnected:
    #  print "Connected to Server"
    #else:
    #  print "Disconnected from Server"

  return

def SocketConnect():
  global SocketConnected

  if not SocketConnected:  
    Socket.connect((Host, Port))
    SetSocketConnectedInternal(True)

  return 
  
def SocketDisconnect():
  global SocketConnected

  if SocketConnected:
    try:
      SetSocketConnectedInternal(False)
      Socket.shutdown()
    except:
      pass

  return
  
def SocketIsReadable():
  if not SocketConnected:
    Result = False
  else:
    ReadableSockets, WritableSockets, ErrorSockets = select.select([Socket], [], [], 0)
    Result = len(ReadableSockets) > 0
  
  return Result
  
def ReceiveBytes(aNumBytes):
  Result = ""
  try:
    while len(Result) != aNumBytes:
      Received = Socket.recv(aNumBytes - len(Result))
      if not Received:
        raise Exception("Socket disconnected while reading")
      SetSocketConnectedInternal(True)
      Result = Result + Received
      #try:
       # Tasks.DoTasks()
      #except:
      #  pass
  except:
    SocketDisconnect()
    raise
      
  return Result

# Connect will not work if socket is disconnected from the peer, 
# but our socket has not picked this up yet. To do this, it need 
# data to be written with send/send all onto it.
# Therefore we write first, and then we check to connect
def SendBytes(aBuffer):
  global SocketConnected
  try:
    Socket.sendall(aBuffer)
    #print "SEND:" + aBuffer
    SetSocketConnectedInternal(True)
  except:
    SocketDisconnect()
    raise  
  return
  
########################################################################
## Command packing/unpacking
MaxPacketLengthCharacters = 6
MaxCmdLengthCharacters = 3

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

def ExecCmd(aCmd, aData, aWaitResponse = True, aTimeoutSec = None):

  Result = ""
  
  # Write the command
  try:
    SendBytes(PackCmd(aCmd, aData, aWaitResponse))
  except:
    SocketConnect()
    SendBytes(PackCmd(aCmd, aData, aWaitResponse))
      
  # Pick up response
  if aWaitResponse:
    StartTime = time.time()
    while True:
      if SocketIsReadable():
        BufferType = ReceiveBytes(1)
        if BufferType == ctInitiator:
          ProcessInitiatorBuffer()
        else:
          break  # continue the processing in ProcessResultBuffer
      if aTimeoutSec != None:
        if time.time() - StartTime >= aTimeoutSec:
          raise Exception("Timeout in ExecCmd")
      #try:
      #  Tasks.DoTasks()
      #except:
      #  pass
    Result = ProcessResultBuffer(BufferType)    

  return Result

def ProcessInitiatorBuffer():
  
  RequiresResponse = ReceiveBytes(1) == ciRequiresResponse
  ReadBuf = ReceiveBytes(MaxPacketLengthCharacters)
  BytesInPacket = int(ReadBuf)
  CmdStr = ReceiveBytes(MaxCmdLengthCharacters)
  ReadBuf = ReceiveBytes(BytesInPacket - MaxCmdLengthCharacters)

  try:
    Result = ClientProcess.ProcessCommand (int(CmdStr), ReadBuf)
    if RequiresResponse:
	  SendBytes(ctResponse + PadNum(len(Result), MaxPacketLengthCharacters) + Result)
  except:
    Result = "Error" #TODO: Make error take from exception the text
    if RequiresResponse:
      SendBytes(ctResponseException + PadNum(len(Result), MaxPacketLengthCharacters) + Result)

  return

def ProcessResultBuffer(aBufferType):
	
  Response = ReceiveBytes(MaxPacketLengthCharacters)
  BytesInPacket = int(Response)
  Response = ReceiveBytes(BytesInPacket)
    
  if aBufferType == ctResponseException:
    raise Exception(Response)

  return Response
  
def SocketProcess():
	
  global LastAliveSent,LastDataSent

  # Check if it is time to send the keep alive message
  NowTime = time.time()
  if NowTime - LastAliveSent >= AliveSendEvery:
    try:
      ExecCmd(Cmd.cmdAlive, "", False)
    except:
        pass
    LastAliveSent = NowTime
    
  if NowTime - LastDataSent >= DataSendEvery:
    try:
      ExecCmd(Cmd.cmdInsertHum,str(HW.GetHumidity()), False)
      ExecCmd(Cmd.cmdInsertTemp,str(HW.GetTemperature()), False)
    except:
        pass
    LastDataSent = NowTime
    
  # Check incoming messages from the peer
  while SocketConnected and SocketIsReadable():
    try:
      BufferType = ReceiveBytes(1)  # ctInitiator, ctResponse or ctResponseException
      if BufferType == ctInitiator:
        ProcessInitiatorBuffer()
      else:
		# Discard buffer, we have a result that we have not asked for
		# This should never happen
        ProcessResultBuffer(ctResponse)
      #Tasks.DoTasks()
    except:
      pass

  return
