import threading

import RPi.GPIO as gpio
import time

class mydis(threading.Thread):
    
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.trig = 5
        self.echo = 6
        gpio.setmode(gpio.BCM)
        gpio.setup(self.trig, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)
        self.client = client
        
    def getDis(self):
        gpio.output(self.trig, gpio.LOW)
        time.sleep(1)
        gpio.output(self.trig, gpio.HIGH)
        time.sleep(0.00001)
        gpio.output(self.trig, gpio.LOW)
        
        while gpio.input(self.echo) == 0:
            pulse_start = time.time()
        while gpio.input(self.echo) == 1:
            pulse_end = time.time()
        dura = pulse_end-pulse_start
        distance1 = dura * 340 * 100 /2 
        distance = round(distance1,2)
        return distance
    
    def run(self):
        while True:
            dis = self.getDis()
            if 2<dis<400:
                self.client.publish("iot/dis",str(dis))
                # print(str(dis))
            time.sleep(5)
           