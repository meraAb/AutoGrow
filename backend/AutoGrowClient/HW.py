import Adafruit_DHT
import random

def GetHumidity():
  Result = ""
  
  #Connect the sensors
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  Result = humidity
  

  return Result    

def GetTemperature():
  Result = ""
  
  #Connect the sensors
  humidity, temperature = Adafruit_DHT.read_retry(11, 4)
  Result = temperature
  

  return Result   









