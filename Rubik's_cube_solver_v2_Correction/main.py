#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, TextMailbox, NumericMailbox
import random
import os
import sys

'''
  U
L F R B
  D
'''

#port A,B,C,D = D面,L面,F面,R面

ev3 = EV3Brick()

cube_D = Motor(Port.A) #D面
cube_R = Motor(Port.B) #R面
cube_B = Motor(Port.C) #B面
cube_L = Motor(Port.D) #L面

SERVER = 'ev3_04'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.

#DLBR面 馬達控制
def rotate_D(): #綠
    cube_D.run_angle(700, 271, then=Stop.COAST,wait=True)
    print('rotate_D angle : ', cube_D.angle(), file=sys.stderr)
    cube_D.reset_angle(0)

def rotate_D_2times():
    cube_D.run_angle(700, 540, then=Stop.COAST, wait=True)
    print('rotate_D_2times angle : ', cube_D.angle(), file=sys.stderr)
    cube_D.reset_angle(0)
    
def rotate_D_reverse():
    cube_D.run_angle(700, -270, then=Stop.COAST, wait=True)
    print('rotate_D_reverse angle : ', cube_D.angle(), file=sys.stderr)
    cube_D.reset_angle(0)
    
def rotate_L(): #橘
    cube_L.run_angle(700, 270, then=Stop.COAST, wait=True)
    print('rotate_L angle : ', cube_L.angle(), file=sys.stderr)
    cube_L.reset_angle(0)

def rotate_L_2times():
    cube_L.run_angle(700, 540, then=Stop.COAST, wait=True)
    print('rotate_L_2times angle : ', cube_L.angle(), file=sys.stderr)
    cube_L.reset_angle(0)
    
def rotate_L_reverse():
    cube_L.run_angle(700, -270, then=Stop.COAST, wait=True)
    print('rotate_L_reverse angle : ', cube_L.angle(), file=sys.stderr)
    cube_L.reset_angle(0)

def rotate_B(): #白
    cube_B.run_angle(700, 270, then=Stop.COAST, wait=True)
    print('rotate_B angle : ', cube_B.angle(), file=sys.stderr)
    cube_B.reset_angle(0)

def rotate_B_2times():
    cube_B.run_angle(700, 540, then=Stop.COAST, wait=True)
    print('rotate_B_2times angle : ', cube_B.angle(), file=sys.stderr)
    cube_B.reset_angle(0)
    
def rotate_B_reverse():
    cube_B.run_angle(700, -270, then=Stop.COAST, wait=True)
    print('rotate_B_reverse angle : ', cube_B.angle(), file=sys.stderr)
    cube_B.reset_angle(0)

def rotate_R(): #紅
    cube_R.run_angle(700, 270, then=Stop.COAST, wait=True)
    print('rotate_R angle : ', cube_R.angle(), file=sys.stderr)
    cube_R.reset_angle(0)

def rotate_R_2times():
    cube_R.run_angle(700, 540, then=Stop.COAST, wait=True)
    print('rotate_R_2times angle : ', cube_R.angle(), file=sys.stderr)
    cube_R.reset_angle(0)
    
def rotate_R_reverse():
    cube_R.run_angle(700, -270, then=Stop.COAST, wait=True)
    print('rotate_R_reverse angle : ', cube_R.angle(), file=sys.stderr)
    cube_R.reset_angle(0)


#UF面 server端 馬達控制
def rotate_U(): #藍
    mbox.send('rotate_U')
    mbox.wait()
    print(mbox.read())

def rotate_U_2times():
    mbox.send('rotate_U_2times')
    mbox.wait()
    print(mbox.read())
    
def rotate_U_reverse():
    mbox.send('rotate_U_reverse')
    mbox.wait()
    print(mbox.read())
    
def rotate_F(): #黃
    mbox.send('rotate_F')
    mbox.wait()
    print(mbox.read())

def rotate_F_2times():
    mbox.send('rotate_F_2times')
    mbox.wait()
    print(mbox.read())

def rotate_F_reverse():
    mbox.send('rotate_F_reverse')
    mbox.wait()
    print(mbox.read())


'''
#test
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
'''


#隨機打亂
random_length = 30
random_array = [0 for j in range(random_length)] #隨機長度
for i in range (random_length):
    random_num = random.randint(1,12)
    while random_num == random_array[i-1]+6 or random_num == random_array[i-1]-6:
        random_num = random.randint(1,12)
    random_array[i] = random_num
    wait(150)
    if random_num == 1:
        rotate_U()
    elif random_num == 2:
        rotate_L()
    elif random_num == 3:
        rotate_F()
    elif random_num == 4:
        rotate_R()
    elif random_num == 5:
        rotate_B()
    elif random_num == 6:
        rotate_D()
    elif random_num == 7:
        rotate_U_reverse()
    elif random_num == 8:
        rotate_L_reverse()
    elif random_num == 9:
        rotate_F_reverse()
    elif random_num == 10:
        rotate_R_reverse()
    elif random_num == 11:
        rotate_B_reverse()
    elif random_num == 12:
        rotate_D_reverse()
ev3.speaker.beep()

