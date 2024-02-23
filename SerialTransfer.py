
import serial
import time
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM13"
ser.open()

while true:
    microbitdata = str(ser.readline())
    
    temperature = microbitdata[2:]
    temperature = temperature.replace(" ","")
    temperature = temperature.replace("'","")
    temperature = temperature.replace("\\r\\n","")
    temperature = int(temperature)
    print (temperature)
    
    time.sleep(5)
    
ser.close()    
