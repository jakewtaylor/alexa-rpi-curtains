from fauxmo.plugins import FauxmoPlugin
import time
import RPi.GPIO as GPIO
import os
from gpio import Pins

class MotorPlugin(FauxmoPlugin):
    # Time in seconds to leave the motor running when toggled
    TIME_TO_MOVE = 5

    """
    Initiates the plugin.
    """
    def __init__(self, name: str, port: int) -> None:
        # set default state
        self.state = 'off'

        # initiate the GPIO pins
        Pins.init()

        # Set motor speed
        GPIO.output(self.PWMA, GPIO.HIGH)

        # initiate parent class
        super().__init__(name=name, port=port)

    """
    Turns on the relay channel.
    """
    def on(self) -> bool:
        print('turning on')
        # adjust state
        self.state = 'on'

        try:
            print('moving motor counter clockwise')
            self.configure_counter_clockwise()
            self.motor_on()

            print('waiting....')
            self.wait_for_movement()

            print('motor off')
            self.motor_off()

            return True
        except Exception as e:
            print(str(e))
            self.state = 'unknown'
            return False

    """
    Turns off the relay channel.
    """
    def off(self) -> bool:
        print('turning off')
        # adjust state
        self.state = 'off'

        try:
            print('moving motor clockwise')
            self.configure_clockwise()
            self.motor_on()

            print('spawning shutdown process...')
            pid = os.spawnlp(
                os.P_NOWAIT,
                '/home/pi/alexa-rpi-curtains/motor-shutdown.py',
                'motor-shutdown.py',
                self.TIME_TO_MOVE
            )
            print('spawned ', pid)
            # print('waiting....')
            # self.wait_for_movement()

            # print('motor off')
            # self.motor_off()

            return True
        except:
            self.state = 'unknown'
            return False

    """
    Gets the current state.
    """
    def get_state(self) -> str:
        print('state was asked for, giving:', self.state)
        return self.state

    """
    Tells the motor to spin in a clockwise manner.
    """
    def configure_clockwise(self) -> None:
        GPIO.output(Pins.AIN1, GPIO.HIGH)
        GPIO.output(Pins.AIN2, GPIO.LOW)

    """
    Tells the motor to spin in a counter-clockwise manner.
    """
    def configure_counter_clockwise(self) -> None:
        GPIO.output(Pins.AIN1, GPIO.LOW)
        GPIO.output(Pins.AIN2, GPIO.HIGH)

    """
    Powers up the motor.
    """
    def motor_on(self) -> None:
        GPIO.output(Pins.STBY, GPIO.HIGH)

    """
    Powers down the motor.
    """
    def motor_off(self) -> None:
        GPIO.output(Pins.STBY, GPIO.LOW)

    def wait_for_movement(self) -> None:
        time.sleep(self.TIME_TO_MOVE)
