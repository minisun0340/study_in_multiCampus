import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
led_pin = 26
gpio.setup(led_pin,gpio.OUT)

myservo = 22
angle = 0

gpio.setup(myservo, gpio.OUT)

pwm_servo = gpio.PWM(myservo, 50)
pwm_servo.start(2.5)

def getDuty(angle):
    if angle in (0, 90, 180):
        #입력된 서보의 각도가 아니라 현재 서보의 각도로 변경할 수 있도록 수정 - global 변수로 만들어서 값을 저장
        print("현재 angle: ", angle)
    publisher.single("degree_test", "현재 angle: "+str(angle), hostname="172.30.1.59")
    Duty = 2.5 + (angle * (12.5-2.5))/180
    return Duty

def connect_result(client, userdata, flags, rc):
    print("connect..."+str(rc)) # rc가 0이면 성공 접속, 1이면 실패
    if rc==0 : #연결이 성공하면 구독신청
        client.subscribe("iot/servo")
    else:
        print("연결실패.....")
        
def on_message(client, userdata, message):
    myval = message.payload.decode("utf-8").split(":")
    #print(message.topic+"-----"+myval)
    
    if myval[1] =="led_on":
        print("on")
        gpio.output(led_pin,gpio.HIGH)
    elif myval[1] == "led_off":
        print("off")
        gpio.output(led_pin, gpio.LOW)
    elif myval[0] == "plus":
        print("플러스")
        pwm_servo.ChangeDutyCycle(getDuty(int(myval[1]))) 
    elif myval[0] == "minus":
        print("마이너스")
        pwm_servo.ChangeDutyCycle(getDuty(int(myval[1]))) 
 
    
try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message # 메시지가 broker에서 전달됐을때 콜백함수가 호출되도록 등록
    mqttClient.connect("172.30.1.59",1883,60)
    mqttClient.loop_forever() # 등록한 토픽의 메시지를 broker에서 전송받아야 하므로 대기
except KeyboardInterrupt:
    pass
finally:
    pwm_servo.ChangeDutyCycle(2.5)
    pwm_servo.stop()
    gpio.cleanup()