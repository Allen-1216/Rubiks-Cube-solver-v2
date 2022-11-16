#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, TextMailbox, NumericMailbox
import os
import sys

#port A,B = U面,B面
'''
  U
L F R B
  D
'''

ev3 = EV3Brick()

cube_U = Motor(Port.A) #U面
cube_B = Motor(Port.B) #B面

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.

#mbox.wait()
#print(mbox.read())


while True:
    order = mbox.read()
    if order == 'rotate_U' : #藍
        wait(50)
        cube_U.run_angle(400, -93, then=Stop.COAST, wait=True)
        mbox.send('rotate_U done')
        
    if order == 'rotate_U_2times' :
        wait(50)
        cube_U.run_angle(400, -184, then=Stop.COAST, wait=True)
        mbox.send('rotate_U_2times done')
        
    if order == 'rotate_U_reverse' :
        wait(50)
        cube_U.run_angle(400, 93, then=Stop.COAST, wait=True)
        mbox.send('rotate_U_reverse done')
        
    if order == 'rotate_B' : #白 (現在黃)
        wait(50)
        cube_B.run_angle(400, -92, then=Stop.COAST, wait=True)
        mbox.send('rotate_B done')
        
    if order == 'rotate_B_2times' :
        wait(50)
        cube_B.run_angle(400, -184, then=Stop.COAST, wait=True)
        mbox.send('rotate_B_2times done')
        
    if order == 'rotate_B_reverse' :
        wait(50)
        cube_B.run_angle(400, 92, then=Stop.COAST, wait=True)
        mbox.send('rotate_B_reverse done')
        
    mbox.wait()
    
