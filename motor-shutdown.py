#!/usr/bin/env

import RPi.GPIO as GPIO
import time
import sys

wait_time = sys.argv[1]
stby = sys.argv[2]

print('wait_time and stby: ', wait_time, stby)

time.sleep(wait_time)
GPIO.output(stby, GPIO.LOW)
