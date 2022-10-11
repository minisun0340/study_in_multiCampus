import paho.mqtt.client as mqtt
from mysensor import PirSensor
from threading import Thread, Event
from led import LED

#시그널을 관리하는 객체
import signal

#Event 객체 - 쓰레드 간의 간단한 통신을 위해 사용되는 객체 - 키보드 인터럽트 시그널을 감지하고 미리 등록한 이벤트가 발생했을 때
# 처리할 함수가 실행되도록 구현
# 1. 이벤트객체를 만들기
#    내부적으로 flag변수를 갖고 있다. 
#    is_set : 내부플래그가 True로 설정되었으면 True를 반환
#    set : 내부플래그를 True로 설정
# 2. 이벤트가 발생되면 실행할 callback함수를 정의
# 3. 키보드인터럽트 시그널을 리스닝하고 있다가 이벤트가 발생하면 반응할 수 있도록 등록 - signal함수가 담당
class MqttWorker:
    def __init__(self): #초기화
        self.client = mqtt.Client()
        self.client.on_connect = self.connect_result
        self.client.on_message = self.on_message
        
        # 1. 이벤트 객체 생성
        self.exit_event = Event()
        
        
        self.pir = PirSensor(self.client)
        self.led = LED()
        self.pir.start()
    
    # 2. 키보드 인터럽트가 발생되면서 이벤트가 발생되면 호출할 콜백함수
    def signal_handler(self, signum, frame):
        print("signal_handler+++++++++++++++++++++++++++++++++++++++")
        self.exit_event.set() # 이벤트객체가 갖고 있는 플래그변수가 True로 세팅
        self.led.clean()
        # 현재 이벤트 발생을 체크하고 다른 작업을 수행하기 위한 코드 - 다른 메소드에서 처리
        if self.exit_event.is_set():
            print("이벤트객체의 플래그변수가 True로 바뀜- 이벤트가 발생하면 어떤 작업을 실행하기 위해서(다른 메소드 내부에서 반복문 빠져나오기) 코드를 정의")
            exit(0)
        
    def mymqtt_connect(self):
        try:
            print("브로커 연결 시작")
            self.client.connect("172.30.1.59", 1883, 60)
            # 키보드 인터럽트(signal.SIGINT) 시그널을 리스닝하고 있다가 키보드 인터럽트가 발생되면 등록한 함수를 호출
            signal.signal(signal.SIGINT, self.signal_handler)
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