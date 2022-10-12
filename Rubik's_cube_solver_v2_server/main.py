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

#port A,B,C,D = D面,L面,F面,R面

ev3 = EV3Brick()

cube_D = Motor(Port.A) #D面
cube_L = Motor(Port.B) #L面
cube_F = Motor(Port.C) #F面
cube_R = Motor(Port.D) #R面

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

def rotate_U():
    mbox.send('rotate_U')
    mbox.wait_new()
    print(mbox.read())

def rotate_U_2times():
    mbox.send('rotate_U_2times')
    mbox.wait_new()
    print(mbox.read())
    
def rotate_U_reverse():
    mbox.send('rotate_U_reverse')
    mbox.wait_new()
    print(mbox.read())
    
def rotate_B():
    mbox.send('rotate_B')
    mbox.wait_new()
    print(mbox.read())

def rotate_B_2times():
    mbox.send('rotate_B_2times')
    mbox.wait_new()
    print(mbox.read())

def rotate_B_reverse():
    mbox.send('rotate_B_reverse')
    mbox.wait_new()
    print(mbox.read())
    
# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.

mbox.wait()
print(mbox.read())

cube_D.run_angle(300, 90*0.6, then=Stop.HOLD, wait=True)
wait(1000)
cube_L.run_angle(300, 90*0.6, then=Stop.HOLD, wait=True)
wait(1000)
rotate_U()
wait(1000)
rotate_U_2times()
wait(1000)
rotate_B()
wait(1000)
rotate_B_2times()
'''
while True:
    mbox.wait_new()
    print(mbox.read())
    mbox.send('RunMotorA')
    break
'''
