#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, TextMailbox, NumericMailbox

#port A,B = U面,B面

ev3 = EV3Brick()

motorA = Motor(Port.A)
SERVER = 'ev3_03'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.

mbox.send('hello!')
mbox.wait()
print(mbox.read())
num = mbox.read()

if num == 'RunMotorA' :
    motorA.run_time(300, 5000, then=Stop.HOLD, wait=True)
    print('motorA done')
    
mbox.wait_new()
