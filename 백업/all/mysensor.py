from threading import Thread
import paho.mqtt.publish as pub
import time
import RPi.GPIO as gpio
import board #데이터 송신용board모듈
import adafruit_dht

class myPir(Thread):
    def __init__(self):
        super().__init__()
        self.pir_pin = 26
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pir_pin, gpio.IN)
        #self.client = client
    def run(self):
        try:
            while True:
                if gpio.input(self.pir_pin) == 1:
                    print("motion detected")
                    pub.single("iot/pir", "motion detected", hostname="172.30.1.33")
                else:
                    print("no motion")
                time.sleep(2)
        except KeyboardInterrupt:
            pass
        finally:
            gpio.cleanup()
                
class myDht(Thread):
    def __init__(self):
        super().__init__()
        self.mydht11 = adafruit_dht.DHT11(board.D19)

    def run(self):
        while True:
            try:
                humid = self.mydht11.humidity
                temp = self.mydht11.temperature
                print(temp, humid)
                pub.single("iot/dht", "temp:"+str(temp) , hostname="172.30.1.33")
                pub.single("iot/dht", "humid:"+str(humid), hostname="172.30.1.33")
                time.sleep(2)
            except RuntimeError as error:
                print(error.args[0])
            finally:
                pass 
        
class myHC(Thread):
    def __init__(self):
        super().__init__()
        self.triger = 5
        self.echo = 6
        gpio.setmode(gpio.BCM)
        gpio.setup(self.triger, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)
    def getDistance(self):
        gpio.output(self.triger, False)
        time.sleep(1)
        gpio.output(self.triger, True)
        time.sleep(0.00001)
        gpio.output(self.triger, False)
        
        while gpio.input(self.echo) == 0:
            pulse_start = time.time()
        
        while gpio.input(self.echo) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 340 * 100 /2
        distance = round(distance, 2)
        return distance
    def run(self):
        try:
            while True:
                dis_val = self.getDistance()
                if 2<dis_val<400:
                    print("distance: % .2f cm" % dis_val)
                    pub.single("iot/hc", "distance:"+str(dis_val), hostname="172.30.1.33")
                    time.sleep(2)
                    
                else:
                    print("범위벗어남")
        except KeyboardInterrupt:
            pass
        finally:
            gpio.cleanup()