#!/usr/bin/python

from datetime import datetime
import serial

serial_ob = serial.Serial(port="/dev/ttyUSB0",baudrate=115200)
filename = datetime.now().strftime("datalog_%Y%m%d_%H%M%S")

try:
    while True:
        serial_log = open(filename + '.csv','a')
        serial_log.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f,"))

                +str(serial_ob.readline()))
        serial_log.close()
except KeyboardInterrupt:
    pass