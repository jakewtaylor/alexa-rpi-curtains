import RPi.GPIO as GPIO

class Pins:
    # GPIO Pin Reference
    PWMA = 7
    AIN2 = 11
    AIN1 = 12
    STBY = 13

    @staticmethod
    def init():
        # initiate the GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(Pins.PWMA, GPIO.OUT)
        GPIO.setup(Pins.AIN2, GPIO.OUT)
        GPIO.setup(Pins.AIN1, GPIO.OUT)
        GPIO.setup(Pins.STBY, GPIO.OUT)