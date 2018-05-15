import time
import TCP

########################################################################
## Main code
while True:
  try:
    TCP.SocketProcess()
  except:
    pass


  # Allow the processor to context switch 
  # and also to lower the power consumption
  time.sleep(0.01)
