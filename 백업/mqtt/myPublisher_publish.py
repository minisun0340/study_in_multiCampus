import paho.mqtt.client as client

# mqttClient객체가 가지고 있는 publish메소드를 사용 - 객체를 생성
'''
 paho.mqtt.client모듈의 Client 객체의 publish를 사용하기 위한 방법
 publish는 메시지를 전송하고 다시 결과를 가지고 되돌아온다.
  1. 클라이언트 객체를 만들기
  2. 클라이언트가 브로커에 연결하기
  3. 메시지 보내기
  4. 메시지를 보낸 후 되돌아오는 결과를 확인
  5. on_publish 콜백을 적용해서 publish가 제대로 됐는지 확인
  
# min : 메시지 id
'''
def publish_ok(client, userdata, mid):
    print(client, userdata, mid)
    print("데이터 전송")


try:
    mqttClient = client.Client("python_pc_pub")
    mqttClient.connect("172.30.1.59", 1883)
    #메시지를 전송하고 되돌아왔을 때 발생되는 이벤트가 on_publish이고 이벤트가 발생되면 callback함수를 실행할 수 있도록 연결
    #메시지를 보내고 되돌아왔을 때 publish_ok 함수를 호출해라
    mqttClient.on_publish = publish_ok
    result = mqttClient.publish("iot/led", "hello?")
    print("호출결과", result)
    mqttClient.loop(2)
except Exception as err:
    print("error", err)