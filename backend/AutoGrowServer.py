import time
import TCPSrv

########################################################################
## Main code
while True:
  try:
    TCPSrv.SocketProcess()
  except:
    pass


  # Allow the processor to context switch 
  # and also to lower the power consumption
  time.sleep(0.01)
