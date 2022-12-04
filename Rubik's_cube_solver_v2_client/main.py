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

#mbox.send('hello!')
#mbox.wait()
#print(mbox.read())

#DLFR面 馬達控制
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

def rotate_B(): #黃 (目前白)
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


#UB面 server端 馬達控制
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
    
def rotate_F(): #白 (目前黃)
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
    


#cube_x, cube_y = 6, 9
cube_list = 54
#cube2d = [[0 for j in range(cube_y)] for k in range(cube_x)] #儲存掃描顏色的2維陣列
cube1d = [0 for i in range(cube_list)] #儲存掃描顏色的1維陣列

# pixy2掃描魔術方塊，取得顏色狀態，透過arduino輸出txt檔案到專案資料夾，再由這裡讀取txt狀態(最後一行)
#如果最後一行不是54個結果，往上一行搜尋
with open('teraterm.txt', 'r') as f:
    txtnum = -1
    totalnum = 54
    content = list(f.readlines())
    last_line = content[txtnum]
    while len(last_line) != totalnum:
        totalnum = 56
        txtnum -= 1
        last_line = content[txtnum]
    print('Arduino傳過來的字串:', last_line, file=sys.stderr)
    print(file=sys.stderr)
x = 0
y = 0
for k in range(54):
    cube1d[k] = last_line[k]
    #cube2d[x][y] = last_line[k]
    y += 1
    if y > 8:
        y = 0
        x += 1

simulation_cube1d = cube1d.copy() #複製一個新一維陣列 符合ULFRBD順序
simulation_cube1d = [element.replace('L', 'N') for element in simulation_cube1d] #交換L跟R
simulation_cube1d = [element.replace('R', 'L') for element in simulation_cube1d]
simulation_cube1d = [element.replace('N', 'R') for element in simulation_cube1d]

print('LR交換後的一維陣列: ', file=sys.stderr)
for i in range(54):
    print(simulation_cube1d[i], end=' ', file=sys.stderr)
    if (i+1) % 9 == 0:
        print(file=sys.stderr)
print(file=sys.stderr)

#新增一個新字串 儲存符合kociemba排列順序 URFDLB
kociemba_cube1d = \
 str(simulation_cube1d[0]) + str(simulation_cube1d[1]) + str(simulation_cube1d[2]) + str(simulation_cube1d[3]) + 'U' + str(simulation_cube1d[5]) + str(simulation_cube1d[6]) + str(simulation_cube1d[7]) + str(simulation_cube1d[8])\
+str(simulation_cube1d[27]) + str(simulation_cube1d[28]) + str(simulation_cube1d[29]) + str(simulation_cube1d[30]) + 'R' + str(simulation_cube1d[32]) + str(simulation_cube1d[33]) + str(simulation_cube1d[34]) + str(simulation_cube1d[35])\
+str(simulation_cube1d[18]) + str(simulation_cube1d[19]) + str(simulation_cube1d[20]) + str(simulation_cube1d[21]) + 'F' + str(simulation_cube1d[23]) + str(simulation_cube1d[24]) + str(simulation_cube1d[25]) + str(simulation_cube1d[26])\
+str(simulation_cube1d[45]) + str(simulation_cube1d[46]) + str(simulation_cube1d[47]) + str(simulation_cube1d[48]) + 'D' + str(simulation_cube1d[50]) + str(simulation_cube1d[51]) + str(simulation_cube1d[52]) + str(simulation_cube1d[53])\
+str(simulation_cube1d[9]) + str(simulation_cube1d[10]) + str(simulation_cube1d[11]) + str(simulation_cube1d[12]) + 'L' + str(simulation_cube1d[14]) + str(simulation_cube1d[15]) + str(simulation_cube1d[16]) + str(simulation_cube1d[17])\
+str(simulation_cube1d[36]) + str(simulation_cube1d[37]) + str(simulation_cube1d[38]) + str(simulation_cube1d[39]) + 'B' + str(simulation_cube1d[41]) + str(simulation_cube1d[42]) + str(simulation_cube1d[43]) + str(simulation_cube1d[44])

print('符合kociemba排序的字串:', kociemba_cube1d, file=sys.stderr)

if kociemba_cube1d == 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB': #檢查現在狀態是否已還原
    print(file=sys.stderr)
    print("*****************************************************", file=sys.stderr)
    print("******************已還原魔術方塊**********************", file=sys.stderr)
    print("*****************************************************", file=sys.stderr)
    print(file=sys.stderr)

#狀態傳入kociemba演算法取得解法
else:
    rubikstring = "kociemba" + " " + kociemba_cube1d
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
    ev3.speaker.beep()


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


#隨機打亂方塊
wait(10000)
random_length = 30
random_array = [0 for j in range(random_length)] #隨機長度
for i in range (30):
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
