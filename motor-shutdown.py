#!/home/pi/.venv/bin/python

import RPi.GPIO as GPIO
import time
import sys
from gpio import Pins

wait_time = int(sys.argv[1])

print('wait_time and stby: ', wait_time, Pins.STBY)

Pins.init()

#time.sleep(wait_time)
select.select([],[],[],wait_time)
GPIO.output(Pins.STBY, GPIO.LOW)
