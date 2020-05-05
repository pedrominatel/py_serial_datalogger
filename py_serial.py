#!/usr/bin/python

from datetime import datetime
import serial
import time

filename = datetime.now().strftime('datalog_%Y%m%d_%H%M%S')
serial_log = open(filename + '.csv','a')

#Mudar port de acordo com a porta serial do gateway
#serial_ob = serial.Serial(port='COM5', baudrate=115200)
serial_ob = serial.Serial(port="/dev/ttyUSB0",baudrate=115200)

time.sleep( 1 )
serial_ob.write(b'AT+START\r')
time.sleep( 1 )

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