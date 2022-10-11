from threading import Thread
import time
import RPi.GPIO as gpio

led_pin = 26
gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

def blink_led():
    while True:
        gpio.output(led_pin, True)
        time.sleep(1)
        gpio.output(led_pin, False)
        time.sleep(1)
    
try:
    mythread = Thread(target=blink_led)
    mythread.start()
    while True:
        print("main쓰레드")
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()