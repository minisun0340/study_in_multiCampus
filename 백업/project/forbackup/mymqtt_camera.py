
from threading import Thread
import paho.mqtt.client as mqtt
import time

from camerapub import Mycamera
from camerapub_thread import camerapub
from threading import Event
import RPi.GPIO as gpio
import signal
from distance import mydis

class mymqttworker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_msg
        
        
        #카메라 관련
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
        
    def on_connect(self, client, userdata, flage, rc):
        print("connecting"+str(rc))
        if rc == 0: #성공
            client.subscribe("mypet/#")
            client.subscribe("iot/led")
            client.subscribe("camerachk")
            time.sleep(1)
        else:
            print("connection fail")
            
    def on_msg(self, client, userdata, message):
        memo = message.payload.decode("utf-8")
        print(message.topic+" "+memo)
        #pet
        if message.topic == "mypet/feed":
            print("도어오픈")
            self.mypetfeed.manualrun()
        elif message.topic == "mypet/water":
            print("워터오픈")
            self.waterSensor.manualrun()
        elif message.topic == "mypet/setTime":
            timearray = memo.split("/")
            self.mypetfeed.setfeedtime(timearray[0], timearray[1])
        #led, curtain
        elif message.topic == "iot/led":
            if memo == "led_on":
                self.led.led_on()
            elif memo == "led_off":
                self.led.led_off()    
            elif memo == "servo_open":
                self.curtain.servo_open()
            elif memo == "servo_close":
               self.curtain.servo_close()    
        elif message.topic == "mypet/setTimeA":
            timearray = memo.split("/")
            time1 = timearray[0].split(":")
            time2 = timearray[1].split(":")
            time1_hour = time1[0]
            time1_min = time1[1]
            time2_hour = time2[0]
            time2_min = time2[1]
            if int(time1_hour) < 10:
                time1_hour = "0"+time1_hour
            if int(time1_min) < 10:
                time1_min = "0"+time1_min
            if int(time2_hour) < 10:
                time2_hour = "0"+time2_hour
            if int(time2_min) < 10:
                time2_min = "0"+time2_min
            
            self.mypetfeed.setfeedtime(time1_hour+":"+time1_min, time2_hour+":"+time2_min)
        #cctv    
       
        if memo == "start" and self.camerachkcnt == 0 :
            self.camerapub = camerapub(self.camera) 
            self.camerachkcnt = 1 
            self.camerapub.start()
        elif memo == "stop":
            self.camerapub.timechk.count = 1
            self.camerachkcnt = 0

    def working(self):
        try:
            self.client.connect("172.30.1.58", 1883, 60)
            signal.signal(signal.SIGINT,self.signal_handler)
            obj = Thread(target=self.client.loop_forever)
            obj.start()
        except KeyboardInterrupt:
            pass
        finally:
            pass