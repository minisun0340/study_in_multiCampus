import paho.mqtt.client as client
import paho.mqtt.publish as publisher
from camerapub_thread import camerapub
from camerapub import Mycamera
from threading import Event
import RPi.GPIO as gpio
import signal
import threading
from distance import mydis

class cameramqtt:
    def __init__(self):
        self.client = client.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.camera = Mycamera()
        self.distance = mydis(self.client)
        self.exit_event = Event()
        self.camerachkcnt = 0
        self.distance.start()
        
    def signal_handler(self,signum,frame):
        self.exit_event.set()
        gpio.cleanup()
        if self.exit_event.is_set() == True:
            exit(0)
        
        
    def mqtt_connect(self):
        try:
            self.client.connect("172.30.1.58",1883,60)
            signal.signal(signal.SIGINT,self.signal_handler)
            mythreadobj = threading.Thread(target=self.client.loop_forever)
            mythreadobj.start()
            
        except KeyboardInterrupt:
            pass
        finally:
            print("종료")
            
    def on_connect(self,client,userdata,flags,rc):
        if rc == 0:
            print("연결 완료")
            client.subscribe("camerachk")
        else:
            print("연결 실패")
    
    def on_message(self,client,userdate,message):
        try:
            cameval = message.payload.decode("utf-8")
            print(cameval)
            if cameval == "start" and self.camerachkcnt == 0:
                self.camerapub = camerapub(self.camera) 
                self.camerachkcnt = 1 
                self.camerapub.start()
            elif cameval == "stop":
                self.camerapub.timechk.count = 1
                self.camerachkcnt = 0
        except:
            pass
        finally:
            pass
        