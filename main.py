import time
import serial
import threading

# Byte translation
READ_CHIP = b'\x02\x00\x09\xFF\xB0\x01\x00\x18\x43'
NO_TRANSPONDER = b'\x02\x00\x08\x00\xb0\x01\x19\xce'

def sendCommand(command):
    connection.write(command)

def receiveThread():
    incoming_byte = connection.read(size=64)
    print(f"read: {incoming_byte}")

# Establish serial connection with correct parameters (check isostart)
connection = serial.Serial("COM9", 9600, timeout=1)
connection.close()
connection.open()

# Receive thread to check for incoming bitstream
receive_thread = threading.Thread(target=receiveThread, args=())
receive_thread.start()

sendCommand(READ_CHIP)
