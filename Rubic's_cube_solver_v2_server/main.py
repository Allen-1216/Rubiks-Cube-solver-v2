#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


from pybricks.messaging import BluetoothMailboxServer, BluetoothMailboxClient, TextMailbox, NumericMailbox

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.

mbox.wait()
print(mbox.read())
mbox.send('RunMotorA')

while True:
    mbox.wait_new()
    print(mbox.read())
    mbox.send('RunMotorA')
    break

