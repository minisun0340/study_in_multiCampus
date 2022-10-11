import paho.mqtt.client as mqtt
import RPi.GPIO as gpio


class LED:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.led_pin = 21
        gpio.setup(self.led_pin,gpio.OUT) 
        
    def led_on(self):
        gpio.output(self.led_pin,gpio.HIGH)
        
    def led_off(self):
        gpio.output(self.led_pin,False)
        
    def clean(self):
        gpio.cleanup()