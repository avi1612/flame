import serial
import time
print('This program allows a user to turn an LED on and on')
ser = serial.Serial('COM4', 115200, timeout=1)
time.sleep(20)

user_input = 'L'
while user_input != 'r':
    user_input = input('H = on, L = off, q = quit :' )
    byte_command = user_input.encode()
    ser.writelines(byte_command)   # send a byte
    time.sleep(0.52) # wait 0.5 seconds

print('q entered. Exiting the program')
ser.close()
print("done")
