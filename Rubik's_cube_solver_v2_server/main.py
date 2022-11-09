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
cube_L = Motor(Port.B) #L面
cube_F = Motor(Port.C) #F面
cube_R = Motor(Port.D) #R面

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

#DLFR面 server端 port motor order
def rotate_D(): #綠
    cube_D.run_angle(400, 94*0.6, then=Stop.COAST,wait=True)
    cube_D.reset_angle(0)

def rotate_D_2times():
    cube_D.run_angle(400, 180*0.6, then=Stop.COAST, wait=True)
    cube_D.reset_angle(0)
    
def rotate_D_reverse():
    cube_D.run_angle(400, -96*0.6, then=Stop.COAST, wait=True)
    cube_D.reset_angle(0)
    
def rotate_L(): #橘
    cube_L.run_angle(400, 98*0.6, then=Stop.COAST, wait=True)
    cube_L.reset_angle(0)

def rotate_L_2times():
    cube_L.run_angle(400, 180*0.6, then=Stop.COAST, wait=True)
    cube_L.reset_angle(0)
    
def rotate_L_reverse():
    cube_L.run_angle(400, -96*0.6, then=Stop.COAST, wait=True)
    cube_L.reset_angle(0)

def rotate_F(): #黃
    cube_F.run_angle(400, 94*0.6, then=Stop.COAST, wait=True)
    cube_F.reset_angle(0)

def rotate_F_2times():
    cube_F.run_angle(400, 180*0.6, then=Stop.COAST, wait=True)
    cube_F.reset_angle(0)
    
def rotate_F_reverse():
    cube_F.run_angle(400, -96*0.6, then=Stop.COAST, wait=True)
    cube_F.reset_angle(0)

def rotate_R(): #紅
    cube_R.run_angle(400, 94*0.6, then=Stop.COAST, wait=True)
    #cube_R.reset_angle(0)

def rotate_R_2times():
    cube_R.run_angle(400, 180*0.6, then=Stop.COAST, wait=True)
    cube_R.reset_angle(0)
    
def rotate_R_reverse():
    cube_R.run_angle(400, -92*0.6, then=Stop.COAST, wait=True)
    cube_R.reset_angle(0)

#UB面 Client端 port motor order
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
    
def rotate_B(): #白
    mbox.send('rotate_B')
    mbox.wait()
    print(mbox.read())

def rotate_B_2times():
    mbox.send('rotate_B_2times')
    mbox.wait()
    print(mbox.read())

def rotate_B_reverse():
    mbox.send('rotate_B_reverse')
    mbox.wait()
    print(mbox.read())
    

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.

mbox.wait()
print(mbox.read())

'''
#隨機打亂方塊
for i in range(20):
    randomnum = random.randint(1,12)
    wait(500)
    if randomnum == 1:
        rotate_U()
    elif randomnum == 2:
        rotate_L()
    elif randomnum == 3:
        rotate_F()
    elif randomnum == 4:
        rotate_R()
    elif randomnum == 5:
        rotate_B()
    elif randomnum == 6:
        rotate_D()
    elif randomnum == 7:
        rotate_U_reverse()
    elif randomnum == 8:
        rotate_L_reverse()
    elif randomnum == 9:
        rotate_F_reverse()
    elif randomnum == 10:
        rotate_R_reverse()
    elif randomnum == 11:
        rotate_B_reverse()
    elif randomnum == 12:
        rotate_D_reverse()
'''

'''
cube_x, cube_y = 6, 9
cube3d = [[0 for j in range(cube_y)] for k in range(cube_x)] #儲存掃描顏色的2維陣列

simulation_cube3d = cube3d.copy() #複製一個新陣列 模擬方塊當下的狀態
kociemba_cube3d = cube3d.copy() #複製一個新陣列 儲存符合kociemba排列順序

#
#
# 這裡寫掃描魔術方塊，取得顏色狀態部分
#
#

if kociemba_cube3d == 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB':
    print("已還原魔術方塊", file=sys.stderr)
#狀態傳入kociemba演算法取得解法
else:
    rubikstring = "kociemba" + " " + kociemba_cube3d
    solvestep = os.popen(rubikstring).read() #透過終端機取得演算法解法
    print('kociemba演算法解法: ' + solvestep, file=sys.stderr)
    
    solvestep2 = solvestep.split(' ') #分割解法字串
    
    for i in range (len(solvestep2)):
        if solvestep2[i] == "U":
            rotate_U()
        elif solvestep2[i] == "L":
            rotate_L()
        elif solvestep2[i] == "F":
            rotate_F()
        elif solvestep2[i] == "R":
            rotate_R()
        elif solvestep2[i] == "B":
            rotate_B()
        elif solvestep2[i] == "D":
            rotate_D()

        elif solvestep2[i] == "U'":
            rotate_U_reverse()
        elif solvestep2[i] == "L'":
            rotate_L_reverse()
        elif solvestep2[i] == "F'":
            rotate_F_reverse()
        elif solvestep2[i] == "R'":
            rotate_R_reverse()
        elif solvestep2[i] == "B'": 
            rotate_B_reverse()
        elif solvestep2[i] == "D'":
            rotate_D_reverse()
            
        elif solvestep2[i] == "U2":
            rotate_U_2times()
        elif solvestep2[i] == "L2":
            rotate_L_2times()
        elif solvestep2[i] == "F2":
            rotate_F_2times()
        elif solvestep2[i] == "R2":
            rotate_R_2times()
        elif solvestep2[i] == "B2":
            rotate_B_2times()
        elif solvestep2[i] == "D2":
            rotate_D_2times()
'''


'''
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