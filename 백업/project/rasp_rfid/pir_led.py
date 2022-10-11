from threading import Thread
import paho.mqtt.publish as publish
import RPi.GPIO as g
import time

class Pir(Thread):
    def __init__(self,rfid):
        super().__init__()
        self.rfid = rfid
        self.pirPin = 23
        self.blueLED = 20
        self.redLED = 21
        g.setmode(g.BCM)
        g.setup(self.pirPin, g.IN)
        g.setup(self.blueLED, g.OUT)
        g.setup(self.redLED, g.OUT)
    
    def led_on(self):
        for i in range(10):
            g.output(self.blueLED, g.HIGH)
            time.sleep(0.5)
            g.output(self.blueLED, g.LOW)
            g.output(self.redLED, g.HIGH)
            time.sleep(0.5)
            g.output(self.redLED, g.LOW)
    
    def run(self):
        while True:
            if self.rfid.access_state['person'] == 0:
                if g.input(self.pirPin) == 1:
                    publish.single("android/pir", "warning", hostname="192.168.50.201")
                    print("보냄")
                    self.led_on()