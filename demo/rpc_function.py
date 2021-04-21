import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

s.write(bytes("\r", 'UTF-8'))
line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
print(line)
line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
print(line)
time.sleep(1)

for i in range(6):
    s.write(bytes("/LEDControl/run 3 1\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

    s.write(bytes("/LEDControl/run 3 0\r", 'UTF-8'))
    line=s.readline() # Read an echo string from mbed terminated with '\n' (putc())
    print(line)
    line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    print(line)
    time.sleep(1)

s.close()