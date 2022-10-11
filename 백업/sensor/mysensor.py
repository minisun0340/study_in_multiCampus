from threading import Thread
from paho.mqtt import publish
import time
import RPi.GPIO as gpio

class PirSensor(Thread):
    def __init__(self):
        super().__init__() #상속받은 클래스의 매개변수 없는 생성자를 호출
        gpio.setmode(gpio.BCM)
        self.pir_pin = 26
        gpio.setup(self.pir_pin, gpio.IN)
        #self.client = client
        
    def run(self):
        while True:
            if gpio.input(self.pir_pin) == 1:
                print("motion detected...")
                publish.single("pir", "motion detected", hostname="172.30.1.59")
            else:
                print("no motion...")
            
            time.sleep(1)
    
    