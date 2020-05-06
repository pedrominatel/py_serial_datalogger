#!/usr/bin/python

from datetime import datetime
import serial
import time
import keyboard


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

        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("q"):  # if key 'q' is pressed 
                print('Finalizando a coleta dos dados...')
                serial_ob.write(b'AT+STOP\r')
                serial_ob.close()
                serial_log.write('### FIM DA COLETA ###')
                serial_log.close()
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break
        
except KeyboardInterrupt:
    print('Finalizando a coleta dos dados...')
    serial_ob.write(b'AT+STOP\r')
    serial_ob.close()
    serial_log.write('### FIM DA COLETA ###')
    serial_log.close()
except:
    print "?"
finally:
    print "Closing...."