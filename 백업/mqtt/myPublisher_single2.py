import paho.mqtt.publish as pub

def publish_ok(client, userdata, mid):
    print(client, userdata, mid)
    print("데이터 전송")
    
try:
    pub.on_publish = publish_ok
    #mqtt Client 객체의 publish처럼 실행하고 결과를 갖고 되돌아오지 않는다. - 작업이 완료되면 연결을 끊는다.
    result = pub.single("test/sensor", "happy", hostname="172.30.1.59")
    print("호출결과=>", result)
except Exception as err:
    print("에러:", err)
