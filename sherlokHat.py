import serial
import webbrowser

port = serial.Serial("/dev/ttyUSB0", baudrate=115200, parity=serial.PARITY_NONE, timeout=3.0)


while True:
    line = str(port.readline())
    if line=="b''":
        continue
    if line[0:16]=="b'Distress call:":
        print("Distress Call Received, tracking link below")
        print(line[18:-3])
        webbrowser.open(line[18:-3])
    if line[0:13]=="b'track Mode:":
        print("Track mode ON, tracking link below")
        print(line[15:-3])
  
    print(line[2:-5])
