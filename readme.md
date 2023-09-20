# Serial communication test

> This script gets available ports then sends and receives data using the ports

- [Serial communication test](#serial-communication-test)
  - [Create virtual ports](#create-virtual-ports)
  - [Requirements](#requirements)
  - [Script documentation](#script-documentation)
  - [Run the script](#run-the-script)


## Create virtual ports

On Debian/Ubuntu distributions we can use socat to create virtual ports, using the command bellow

```bash
#install socat
sudo apt-get install socat
```

In a new terminal, use the following code to create a pair of serial ports connected between them

```bash
sudo socat -d -d pty,raw,echo=0,link=/dev/ttyS0 pty,raw,echo=0,link=/dev/ttyS1
```

## Requirements
Only `pyserial` was required it is also, shown on `requirements.txt`

## Script documentation

```bash
NAME
main

DESCRIPTION
This script list the available ports and selects the
first ones send messages between them.
The script finishes when 10 messages where send and received

    Author: Franco Rosa
    Date: September 20, 2023

FUNCTIONS
    read_data(device)
        This method runs as a thread, the input is the name of the serial port
        it creates a serial port instance and listens to messages over it
        the script finishes when 10 messages are received

    send_data(device)
        This method runs as a thread, the input is the name of the serial port
        it creates a serial port instance and starts sending messages over it
        the script finishes when 10 messages are sent

    sleep(...)
        sleep(seconds)

        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.

DATA
port = <serial.tools.list_ports_linux.SysFS object>
ports = Array of available ports
port1 = First port found
port2 = Second port found
read_thread = thread
send_thread = thread

FILE
/home/fx/Desktop/homework/main.py

```

- The previous documentation was scafolded using pydoc

```bash
pydoc main
```

## Run the script

```bash
python main.py
```