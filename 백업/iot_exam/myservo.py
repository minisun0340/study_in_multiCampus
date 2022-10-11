import RPi.GPIO as gpio
import time


class Servo:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.servo_pin = 19
        gpio.setup(self.servo_pin, gpio.OUT)
        self.pwm = gpio.PWM(self.servo_pin, 50)
        self.pwm.start(3)
    def dooropen(self):
        self.pwm.ChangeDutyCycle(13)
        time.sleep(0.02)
    def doorclose(self):
        self.pwm.ChangeDutyCycle(3)
        time.sleep(0.02)
    def clean(self):
        gpio.cleanup()
        