#!/usr/bin/python

from datetime import datetime
import serial
import time
import sys

#Mudar port de acordo com a porta serial do gateway
COMport = '/dev/ttyUSB0'
COMspeed = 115200

filename = datetime.now().strftime('datalog_%Y%m%d_%H%M%S')
serial_log = open(filename + '.csv','a')

#serial_ob = serial.Serial(port='COM5', baudrate=115200)
serial_ob = serial.Serial(port=COMport,baudrate=COMspeed)

time.sleep( 1 )
serial_ob.write(b'AT+START\r')

try:
    while True:
        
        serial_log.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f,'))
                +str(serial_ob.readline()))
        
except KeyboardInterrupt:
    print('Finalizando a coleta dos dados...')
    serial_ob.write(b'AT+STOP\r')
    serial_ob.close()
    serial_log.write('### FIM DA COLETA ###')
    serial_log.close()
    pass