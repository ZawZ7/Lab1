from pyb import Pin, Timer
import time


class MotorDriver:
    # Constructor to initialize motor control pins and PWM timer
    def __init__(self, en_pin, IN1A_pin, IN2A_pin, PWM_tim):
        """ 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin: Pin connected to the enable pin of the motor driver
        @param IN1A_pin: Pin connected to IN1A of the motor driver
        @param IN2A_pin: Pin connected to IN2A of the motor driver
        @param timer: Timer used for PWM control
        """
        print("Creating a motor driver")
        self.EN = pyb.Pin(en_pin, pyb.Pin.OUT_OD, pyb.Pin.PULL_UP)
        self.IN1A = Pin(IN1A_pin, Pin.OUT_PP)
        self.IN2A = Pin(IN2A_pin, Pin.OUT_PP)

        self.tim = PWM_tim

        self.PWM1 = self.tim.channel(1, mode=Timer.PWM, pin=self.IN1A)  # Initialize PWM channel 1
        self.PWM2 = self.tim.channel(2, mode=Timer.PWM, pin=self.IN2A)  # Initialize PWM channel 2

        self.EN.value(0)

    # Method to set duty cycle for motor control
    def set_duty_cycle(self, duty):
        """
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param duty: A signed integer holding the duty
               cycle of the voltage sent to the motor
        """
        print(f"Setting Duty Cycle to {duty}")

        if duty > 0:
            if duty > 100:
                self.PWM1.pulse_width_percent(100)
            else:
                self.PWM1.pulse_width_percent(duty)  # Set duty cycle for forward motion
            self.PWM2.pulse_width_percent(0)
        elif duty < 0:
            if duty < -100:
                print('here')
                self.PWM2.pulse_width_percent(100)
            else:
                self.PWM2.pulse_width_percent((-1) * duty)  # Set duty cycle for backward motion
            self.PWM1.pulse_width_percent(0)
        else:
            self.PWM1.pulse_width_percent(0)
            self.PWM2.pulse_width_percent(0)
        self.EN.value(1)


#
if __name__ == '__main__':
    # testing the code

    moe = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, pyb.Timer(3, freq=20000))
    moe.set_duty_cycle(-42)
    time.sleep(4)
    moe.set_duty_cycle(73)
    time.sleep(4)
    moe.set_duty_cycle(0)
    time.sleep(4)
    moe.set_duty_cycle(-150)
    time.sleep(4)
    moe.set_duty_cycle(150)
    time.sleep(4)
    moe.set_duty_cycle(0)
