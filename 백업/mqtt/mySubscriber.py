import paho.mqtt.client as mqtt

# broker에 구독신청 - broker와 연결하고 topic을 등록. 연결이 성공하면 메시지 전송받도록 설정
#                                                    ------------- 되돌아와서 callback함수를 호출
# client는 연결했던 정보 콜백을 실행하는 주체 - 현재 작업하고 있는 publisher의 정보

def connect_result(client, userdata, flags, rc):
    print("connect..."+str(rc)) #rc가 0이면 성공접속, 1이면 실패
    if rc==0 : #연결이 성공하면 구독신청
        client.subscribe("iot/#") # iot/로 토픽명이 시작하면 뒤에는 어떤 키워드가 와도 모두 수신
    else :
        print("연결실패...")
        
def on_message(client, userdata, message):
    myval = message.payload.decode("utf-8")
    print(myval)
            

try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message # 메시지가 broker에서 전달됐을 때 콜백함수가 호출되도록 등록
    mqttClient.connect("172.30.1.59", 1883, 60)  #60은 대기시간
    mqttClient.loop_forever()  #등록한 토픽의 메시지를 broker에서 전송받아야 하므로 대기
except KeyboardInterrupt:
    pass
finally:
    pass