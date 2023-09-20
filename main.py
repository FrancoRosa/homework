'''
This script list the available ports and selects the 
first ones send messages between them.
The script finishes when 10 messages where send and received 

Author: Franco Rosa
Date: September 20, 2023
'''

from time import sleep

import serial
import threading
import serial.tools.list_ports as serials


def send_data(device):
    '''
    This method runs as a thread, the input is the name of the serial port
    it creates a serial port instance and starts sending messages over it
    the script finishes when 10 messages are sent
    '''
    sender = serial.Serial(device, 9600)
    t = 0
    print("Sender serial port created!")
    while True:
        sleep(2)
        message = f"Hello {t}"
        print("Sending:", message)
        sender.write(message.encode())
        t = t + 1
        if t > 10:
            break
    sender.close()


def read_data(device):
    '''
    This method runs as a thread, the input is the name of the serial port
    it creates a serial port instance and listens to messages over it
    the script finishes when 10 messages are received
    '''
    listener = serial.Serial(device, 9600)
    t = 1
    sleep(1)
    print("Listener serial port created!")
    while True:
        data = listener.readline().decode().strip()
        if data:
            print(f"Received: {data}")
            t = t + 1
            if t == 10:
                break
    listener.close()


# List available serial ports
ports = list(serials.comports())

if len(ports) < 2:
    print("At least two ports are required.")

else:
    print("Available serial ports:")
    for port in ports:
        print(port.device)

    # Prompt the user to select two serial ports
    port1 = ports[0].device
    port2 = ports[1].device
    print("Port 1:", port1)
    print("Port 2:", port2)

    try:
        # Create threads for sending and receiving data
        send_thread = threading.Thread(target=send_data, args=(port1,))
        read_thread = threading.Thread(target=read_data, args=(port2,))

        # Start the threads
        send_thread.start()
        read_thread.start()

    except serial.SerialException as e:
        print(f"Error opening serial ports: {e}")

print("Program terminated.")
