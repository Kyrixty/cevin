#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random as rn
# Initialize the EV3 Brick.
ev3 = EV3Brick()
obstacle_sensor = UltrasonicSensor(Port.S4)

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for one meter.
ev3.speaker.beep()
while True:
    # Begin driving forward at 200 millimeters per second.
    robot.drive(600, 0)

    # Wait until an obstacle is detected. This is done by repeatedly
    # doing nothing (waiting for 10 milliseconds) while the measured
    # distance is still greater than 300 mm.
    while obstacle_sensor.distance() > 200:
        wait(15)

    # Drive backward for 300 millimeters.
    ev3.speaker.beep()
    robot.turn(rn.randint(10,180))
    # Turn around by 120 degrees
    