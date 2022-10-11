from threading import Thread
import serial
import time
import paho.mqtt.publish as pub
from threading import Thread

class water_pump_sound(Thread):
    def __init__(self):
        super().__init__()
        #처음 시리얼통신 설정 작업-한번만
        self.myserial = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
        self.myserial.flush()
    def manaulwater(self):
        self.myserial.write(bytes("open", "utf-8"))
        
    def run(self):
        while True:
            line = self.myserial.readline().decode("utf-8").rstrip()
            print(line)
            value = line.split(":")
            if value[0]=="wt":
                pub.single("mypet/waterlevel", value[1], hostname="172.30.1.2")
            if value[0]=="sd":
                if int(value[1])>340:
                    print("alert")
                    pub.single("iot/sound", "alert!", hostname="172.30.1.2")