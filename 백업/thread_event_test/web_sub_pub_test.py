import mymqtt as mymqtt
from led import LED


# 테스트작업을 위한 클래스
myled = LED()
if __name__=="__main__":
    try: 
        mqtt = mymqtt.MqttWorker()
        mqtt.mymqtt_connect() #콜백함수가 아니므로 인스턴스 변수를 이용해서 호출해야 한다.
        for i in range(10):
            print(i)
        
    except KeyboardInterrupt:
        pass
    finally:
        print("종료")