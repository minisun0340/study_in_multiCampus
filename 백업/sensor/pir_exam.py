import RPi.GPIO as gpio
import time


led_pin = 21
pir_pin = 26

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)
gpio.setup(pir_pin, gpio.IN)

try:
    while True:
        if gpio.input(pir_pin)==1:
            print("motion detected...")
            gpio.output(led_pin, True)
            
        else:
            gpio.output(led_pin, False)
            print("no motion...")
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    gpio.cleanup()