from picamera import PiCamera
from time import sleep
import paho.mqtt.client as mqtt

def connect_result(client, userdata, flags, rc):
    print("connect..."+str(rc)) #rc가 0이면 성공접속, 1이면 실패
    if rc==0 : #연결이 성공하면 구독신청
        client.subscribe("mydata/file")
        
    else :
        print("연결실패...")
        
def on_message(client, userdata, message):
    try:
        f = open("output.jpg", "w")
        f.write(message.payload)
        print("메시지 수신완료 - 파일 저장하기 완료")
        f.close
    except Exception as err:
        print("에러발생: ", err)
    finally:
        pass


try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message
    mqttClient.connect("172.30.1.59", 1883, 60)
    mqttClient.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    pass