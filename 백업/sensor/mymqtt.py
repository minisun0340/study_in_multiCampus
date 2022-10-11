import paho.mqtt.client as mqtt
from mysensor import PirSensor
from threading import Thread
from led import LED

# mqtt통신관련 작업만 처리하는 클래스
class MqttWorker:
    def __init__(self): #초기화
        self.client = mqtt.Client()
        self.client.on_connect = self.connect_result
        self.client.on_message = self.on_message
        #self.pir = PirSensor(self.client)
        self.led = LED()
        #self.pir.start()
    
    def mymqtt_connect(self):
        try:
            print("브로커 연결 시작")
            self.client.connect("172.30.1.59", 1883, 60)
            mythreadobj = Thread(target=self.client.loop_forever)
            mythreadobj.start() 
        except KeyboardInterrupt:
            pass
        finally:
            print("종료")
    
        
    def connect_result(self, client, userdata, flags, rc):
        print("connect..."+str(rc)) # rc가 0이면 성공 접속, 1이면 실패
        if rc==0 : #연결이 성공하면 구독신청
            client.subscribe("iot/led")
        else:
            print("연결실패.....")
            
    def on_message(self, client, userdata, message): 
        #라즈베리파이가 메시지를 받으면 호출되는 함수이므로 받은 메세지에 대한 처리를 구현
        try:
            print("test")
            myval = message.payload.decode("utf-8")
            print(message.topic+"-----"+myval)
            if myval == "led_on":
                self.led.led_on()
            elif myval == "led_off":
                self.led.led_off()
        except KeyboardInterrupt:
            pass
        finally:
            pass
        
        
        
if __name__=="__main__":
    try:
        mqtt = MqttWorker()
        mqtt.mymqtt_connect()
        for i in range(10):
            print(i)
        
    except KeyboardInterrupt:
        pass
    finally:
        print("종료")