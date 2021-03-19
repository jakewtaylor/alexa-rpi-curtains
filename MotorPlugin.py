from fauxmo.plugins import FauxmoPlugin
import time
import RPi.GPIO as GPIO

class MotorPlugin(FauxmoPlugin):
    # GPIO Pin Reference
    PWMA = 7
    AIN2 = 11
    AIN1 = 12
    STBY = 13

    TIME_TO_MOVE = 5
    OPEN = True

    """
    Initiates the plugin.
    """
    def __init__(self, name: str, port: int) -> None:
        # set default state
        self.state = 'off'

        # initiate the GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.AIN2, GPIO.OUT)
        GPIO.setup(self.AIN1, GPIO.OUT)
        GPIO.setup(self.STBY, GPIO.OUT)

        GPIO.output(self.PWMA, GPIO.HIGH) # Set motor speed

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

            print('waiting....')
            self.wait_for_movement()

            print('motor off')
            self.motor_off()

            return True
        except:
            self.state = 'unknown'
            return False

    """
    Gets the current state.
    """
    def get_state(self) -> str:
        return self.state

    """
    Tells the motor to spin in a clockwise manner.
    """
    def configure_clockwise(self) -> None:
        GPIO.output(self.AIN1, GPIO.HIGH)
        GPIO.output(self.AIN2, GPIO.LOW)

    """
    Tells the motor to spin in a counter-clockwise manner.
    """
    def configure_counter_clockwise(self) -> None:
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.HIGH)

    """
    Powers up the motor.
    """
    def motor_on(self) -> None:
        GPIO.output(self.STBY, GPIO.HIGH)

    """
    Powers down the motor.
    """
    def motor_off(self) -> None:
        GPIO.output(self.STBY, GPIO.LOW)

    def wait_for_movement(self) -> None:
        time.sleep(self.TIME_TO_MOVE)
