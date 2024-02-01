"""! @file led.py
Script to control LED brightness using PWM on STM32L476RG Nucleo board.
"""

import time
import pyb

def led_setup():
    """! Sets up PWM timer and channel for controlling LED brightness.

    Configures Timer 2 Channel 1 for PWM output on pin PA0 (Arduino pin D2).
    """
    global timer, ch
    timer = pyb.Timer(2, freq=1000)  # Timer 2, frequency 1kHz
    ch = timer.channel(1, pyb.Timer.PWM_INVERTED, pin=pyb.Pin.board.PA0)  # Channel 1

def led_brightness(duty_cycle):
    """! Sets LED brightness using PWM duty cycle.

    Args:
        duty_cycle (float): Duty cycle value between 0 and 1.
            0 represents fully off, 1 represents fully on.
    """
    ch.pulse_width_percent(duty_cycle * 100)

if __name__ == "__main__":
    led_setup()

#     transition_duration = 5  # Duration of the brightness transition in seconds
#     steps_per_second = 100   # Number of steps per second
#     total_steps = transition_duration * steps_per_second
#     step_time = transition_duration / total_steps

    while True:
        # Increasing brightness
        for duty_cycle in range(0, 101):
            led_brightness(duty_cycle / 100)
            time.sleep(5/100)

        # Decreasing brightness
        for duty_cycle in range(100, -1, -1):
            led_brightness(duty_cycle / 100)
            time.sleep(5/100)
