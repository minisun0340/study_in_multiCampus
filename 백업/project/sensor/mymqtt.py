from threading import Thread
import paho.mqtt.client as mqtt
import time
from water_pump_sound import water_pump_sound
import RPi.GPIO as gpio


class mymqttworker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_msg
        self.wps = water_pump_sound()
        self.wps.start()
        
    def on_connect(self, client, userdata, flage, rc):
        print("connecting"+str(rc))
        if rc == 0: #성공
            client.subscribe("mypet/water")
            time.sleep(1)
        else:
            print("connection fail")
            
    def on_msg(self, client, userdata, message):
        memo = message.payload.decode("utf-8")
        print(message.topic+" "+memo)
        if message.topic == "mypet/water":
            print("워터오픈")
            self.wps.manaulwater()

    def working(self):
        try:
            self.client.connect("172.30.1.2", 1883, 60)
            obj = Thread(target=self.client.loop_forever)
            obj.start()
        except KeyboardInterrupt:
            pass
        finally:
            pass

if __name__=="__main__":
    try: 
        mmw = mymqttworker()
        mmw.working()
        
    except KeyboardInterrupt:
        pass
    finally:
        pass