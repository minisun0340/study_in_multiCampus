from threading import Thread
import paho.mqtt.client as mqtt
import time
from mydevice import Led

class mymqttworker:
    def __init__(self, topic):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_msg
        self.topic = topic 
        
    def on_connect(self, client, userdata, flage, rc):
        print("connecting"+str(rc))
        if rc == 0: #성공
            client.subscribe(self.topic)
            time.sleep(1)
        else:
            print("connection fail")
    def on_msg(self, client, userdata, message):
        memo = message.payload.decode("utf-8")
        print(message.topic+" "+memo)
        if memo == "led_on":
            myled = Led()
            myled.led_on()
        elif memo == "led_off":
            myled = Led()
            myled.led_off() 
    def working(self):
        try:
            self.client.connect("172.30.1.33", 1883, 60)
            obj = Thread(target=self.client.loop_forever)
            obj.start()
        except KeyboardInterrupt:
            pass
        finally:
            print("working 끝~~~~")
