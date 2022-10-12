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

def rotate_D(): #DLFR面 server端 port motor order
    cube_D.run_angle(500, 90*0.6, then=Stop.HOLD, wait=True)

def rotate_D_2times():
    cube_D.run_angle(500, 180*0.6, then=Stop.HOLD, wait=True)
    
def rotate_D_reverse():
    cube_D.run_angle(500, -90*0.6, then=Stop.HOLD, wait=True)
    
def rotate_L():
    cube_L.run_angle(500, 90*0.6, then=Stop.HOLD, wait=True)

def rotate_L_2times():
    cube_L.run_angle(500, 180*0.6, then=Stop.HOLD, wait=True)
    
def rotate_L_reverse():
    cube_L.run_angle(500, -90*0.6, then=Stop.HOLD, wait=True)

def rotate_F():
    cube_F.run_angle(500, 90*0.6, then=Stop.HOLD, wait=True)

def rotate_F_2times():
    cube_F.run_angle(500, 180*0.6, then=Stop.HOLD, wait=True)
    
def rotate_F_reverse():
    cube_F.run_angle(500, -90*0.6, then=Stop.HOLD, wait=True)

def rotate_R():
    cube_R.run_angle(500, 90*0.6, then=Stop.HOLD, wait=True)

def rotate_R_2times():
    cube_R.run_angle(500, 180*0.6, then=Stop.HOLD, wait=True)
    
def rotate_R_reverse():
    cube_R.run_angle(500, -90*0.6, then=Stop.HOLD, wait=True)

def rotate_U(): #UB面 Client端 port motor order
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


rotate_U()
wait(1000)
rotate_L()
wait(1000)
rotate_F()
wait(1000)
rotate_R()
wait(1000)
rotate_B()
wait(1000)
rotate_D()
wait(1000)

rotate_U_2times()
wait(1000)
rotate_L_2times()
wait(1000)
rotate_F_2times()
wait(1000)
rotate_R_2times()
wait(1000)
rotate_B_2times()
wait(1000)
rotate_D_2times()
wait(1000)

rotate_U_reverse()
wait(1000)
rotate_L_reverse()
wait(1000)
rotate_F_reverse()
wait(1000)
rotate_R_reverse()
wait(1000)
rotate_B_reverse()
wait(1000)
rotate_D_reverse()
wait(1000)