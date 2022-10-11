from threading import Thread
from datetime import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import RPi.GPIO as g
import serial
import dht
import pir_led
import mymqtt
import json


#라즈베리파이에서 아두이노 실행
#아두이노 시리얼 모니터 키면 오류남
uidfileroute = "/home/pi/iot/user.json"
humidFileRoute = "/home/pi/iot/humid.json"
tempFileRoute = "/home/pi/iot/temp.json"
personFileRoute = "/home/pi/iot/person.json"
        

            
class RFID(Thread):
    def __init__(self):
        super().__init__()
        self.btn_save_pin = 17
        self.btn_remove_pin = 27
        self.uid_dic = file.jsonfile(uidfileroute)
        self.btn_state = 0 #버튼 상태
        self.access_state = file.jsonfile(personFileRoute)
        print(self.access_state)
        g.setmode(g.BCM)
        g.setup(self.btn_save_pin, g.IN, pull_up_down=g.PUD_DOWN)
        g.setup(self.btn_remove_pin, g.IN, pull_up_down=g.PUD_DOWN)
        g.add_event_detect(self.btn_save_pin,g.FALLING,callback=self.save, bouncetime=300)
        g.add_event_detect(self.btn_remove_pin,g.FALLING,callback=self.remove, bouncetime=300)
    
    def save(self, channel):
        try:
            if self.btn_state == 0:
                self.btn_state = 1
                print("저장 버튼이 눌림")
            else:
                raise Exception
        except:
            if self.btn_state == 1:
                print("추가 버튼이 이미 눌려졌습니다.")
            elif self.btn_state == 2:
                print("삭제 버튼이 이미 눌려졌습니다.")
    
    def remove(self, channel):
        try:
            if self.btn_state == 0:
                self.btn_state = 2
                print("삭제 버튼이 눌림")
            else:
                raise Exception
        except:
            if self.btn_state == 1:
                print("추가 버튼이 이미 눌려졌습니다.")
            elif self.btn_state == 2:
                print("삭제 버튼이 이미 눌려졌습니다.")
                
    def enter_out(self, msg):
        if self.uid_dic[msg] == 1: #외출하게 되면
            self.uid_dic[msg] = 0
            file.uidchange(msg)
            return 0
        elif self.uid_dic[msg] == 0: #집에 들어오게 되면
            self.uid_dic[msg] = 1
            file.uidchange(msg)
            return 1
        
class FileReadWrite:
    def uidsave(self, msg):
        if msg in rfid.uid_dic: #데이터가 있다면 패스
            print("이미 저장되어 있습니다.")
        else:                   #데이터가 없다면 저장
            rfid.uid_dic[msg] = 1
            with open(uidfileroute, "w") as f:
                json.dump(rfid.uid_dic, f)
            self.personplus()
            print(msg+"저장완료")
    
    def uidremove(self, msg):
        if msg in rfid.uid_dic:
            del rfid.uid_dic[msg]
            with open(uidfileroute, "w") as f:
                json.dump(rfid.uid_dic, f)
            print(msg+"제거 성공")
        else:
            print("데이터가 없습니다.")
        
    def uidchange(self, msg):
        if msg in rfid.uid_dic:
            with open(uidfileroute, "w") as f:
                json.dump(rfid.uid_dic, f)
                    
    def dht_save(self, data, route, dic):
        now = datetime.now()
        current_time = now.strftime("%H/%M/%S")
        if len(dic) > 19:
            dic.pop(next(iter(dic)))
        dic[current_time] = data
        with open(route, "w") as f:
            json.dump(dic, f)
    
    def jsonfile(self, route):
        try:
            with open(route, "r") as f:
                return json.load(f)
        except:
            f = open(route,"w")
        finally:
            f.close()
    
    def personplus(self):
        rfid.access_state['person'] += 1
        with open(personFileRoute, "w") as f:
            json.dump(rfid.access_state, f)
    
    def personminus(self):
        rfid.access_state['person'] -= 1
        if rfid.access_state['person'] < 0:
            rfid.access_state['person'] = 0
        with open(personFileRoute, "w") as f:
            json.dump(rfid.access_state, f)
        
class ArduinoSerail(Thread):
    def __init__(self):
        super().__init__()
        self.port = '/dev/ttyACM0'
        self.serialport = 9600
        self.ser = serial.Serial(self.port, self.serialport, timeout=1)
        self.ser.flush()
        
    def run(self):
        while True:
            if self.ser.in_waiting > 0:
                msg = self.ser.readline().decode('utf-8').rstrip()
                if rfid.btn_state == 1: #추가 버튼이 눌려졌다면
                    file.uidsave(msg)
                    rfid.btn_state = 0
                elif rfid.btn_state == 2: #삭제 버튼이 눌려졌다면
                    file.uidremove(msg)
                    rfid.btn_state = 0
                elif msg in rfid.uid_dic: # 출입 / 외출
                    if rfid.enter_out(msg):
                        file.personplus()
                        print("ddd")
                        publish.single("android/rfid",msg,hostname="192.168.50.201")
                    else:
                        file.personminus()


if __name__ == "__main__" :
    file = FileReadWrite()
    arduino = ArduinoSerail()
    rfid = RFID()
    dht = dht.SEN(file)
    pir = pir_led.Pir(rfid)
    arduino.start()
    rfid.start()
    dht.start()
    pir.start()
    client = mymqtt.Mqtt()
    