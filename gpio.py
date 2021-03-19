import RPi.GPIO as GPIO

class Pins:
    # GPIO Pin Reference
    PWMA = 7
    AIN2 = 11
    AIN1 = 12
    STBY = 13

    @staticmethod
    def init(self):
        # initiate the GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.AIN2, GPIO.OUT)
        GPIO.setup(self.AIN1, GPIO.OUT)
        GPIO.setup(self.STBY, GPIO.OUT)