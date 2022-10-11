import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
ENA = 25
IN1 = 24
IN2 = 23

ENB = 16
IN3 = 21
IN4 = 20

gpio.setup(ENA, gpio.OUT)
gpio.setup(IN1, gpio.OUT)
gpio.setup(IN2, gpio.OUT)

gpio.setup(ENB, gpio.OUT)
gpio.setup(IN3, gpio.OUT)
gpio.setup(IN4, gpio.OUT)

try:
    while True:
        print("동작")
        gpio.output(IN1, True)
        gpio.output(IN2, False)
        gpio.output(ENA, True)
        
        gpio.output(IN3, False)
        gpio.output(IN4, True)
        gpio.output(ENB, True)
        time.sleep(3)
finally:
    gpio.cleanup()