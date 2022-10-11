import mymqtt
from mysensor import PirSensor
from led import LED
import time

myled = LED()
# 테스트작업을 위한 클래스
if __name__=="__main__":
    try: 
        mqtt = mymqtt.MqttWorker()
        mqtt.mymqtt_connect() #콜백함수가 아니므로 인스턴스 변수를 이용해서 호출해야 한다.
        pir = PirSensor()
        pir.start()
        while True:
            time.sleep(1)
        
    except KeyboardInterrupt:
        pass
    finally:
        myled.clean()