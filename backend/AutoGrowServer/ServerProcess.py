import sys,time
import re
import datetime
import Cmd, DB


def ProcessCommand(aSocket, aCmd, aData):

  Result = " "
  
  ip = aSocket.getpeername()[0]
  if aCmd == Cmd.cmdInsertHum:

	print "Data Received from: " + ip 
	print "Humidity is " + aData + " %"
	DB.Cursor.execute("SELECT MAC FROM subnode WHERE IP=%s",(ip))
	MAC = str(DB.Cursor.fetchone()[0])
	
	#Get the time and date
	date = time.strftime('%Y-%m-%d %H:%M:%S')
	query = ("INSERT INTO data "
			"(MAC,SensorId,Date,Value) " 
			"VALUES (%(MAC)s,%(SensorId)s,%(Date)s,%(Value)s)")
			
	args = {
	'MAC': MAC,
	'SensorId': 'SoilHum0',
	'Date': date,
	'Value': aData,
	}

	DB.Cursor.execute(query, args)
	DB.Connection.commit()
	
  elif aCmd == Cmd.cmdInsertTemp:

	print "Data Received from: " + ip 
	print "Temperature is " + aData + " C"
	DB.Cursor.execute("SELECT MAC FROM subnode WHERE IP=%s",(ip))
	MAC = str(DB.Cursor.fetchone()[0])
	
	#Get the time and date
	date = time.strftime('%Y-%m-%d %H:%M:%S')
	query = ("INSERT INTO data "
			"(MAC,SensorId,Date,Value) " 
			"VALUES (%(MAC)s,%(SensorId)s,%(Date)s,%(Value)s)")
	args = {
	'MAC': MAC,
	'SensorId': 'SoilTemp',
	'Date': date,
	'Value': aData,
	}

	DB.Cursor.execute(query, args)
	DB.Connection.commit()  	  
    	  
  return Result
