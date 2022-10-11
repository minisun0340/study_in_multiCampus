import RPi.GPIO as gpio
import time
import paho.mqtt.client as mqtt
from threading import Thread

pir_pin = 26

gpio.setmode(gpio.BCM)
gpio.setup(pir_pin, gpio.IN)

class mypub(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def pub_ok(client, userdata, mid):
        print(client, userdata, mid)
        print("데이터 전송 ok")
    
    def run(self):
        publisher = mqtt.Client()
        publisher.connect("172.30.1.59", 1883)
        publisher.on_publish = mypub.pub_ok
        publisher.publish("pir", "motion detected")

class mypir(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        if gpio.input(pir_pin)==1:
            print("motion detected...")
            pubon = mypub()
            pubon.start()
        else:
            print("no motion...")   
        time.sleep(1)

try:
    while True:
        mypir_on = mypir()
        mypir_on.start()
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    gpio.cleanup()