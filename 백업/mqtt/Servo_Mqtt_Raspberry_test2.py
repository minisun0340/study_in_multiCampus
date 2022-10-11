from math import degrees
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publisher
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
servo_pin = 22
led_pin = 19
gpio.setup(led_pin,gpio.OUT)
gpio.setup(servo_pin, gpio.OUT)  # 서보핀을 출력으로 설정
pwm_servo = gpio.PWM(servo_pin, 50)  # 서보핀을 PWM 모드 50Hz로 사용
pwm_servo.start(2.5)
angle = 0

def getDuty(degree):
    if degree in (0,90,180):
        #입력된 서보의 각도가 아니라 현재 서보의 각도로 변경할 수 있도록 수정 - global변수 만들어서 값을 저장
        for i in range(10):
            publisher.single("degree_test","current_angle: "+str(degree),hostname="172.30.1.59")
    duty = 2.5+ degree*10 /180
    return duty

def connect_result(client, userdata, flags, rc):
    print("connect..."+str(rc)) # rc가 0이면 성공 접속, 1이면 실패
    if rc==0 : #연결이 성공하면 구독신청
        client.subscribe("iot/#")
    else:
        print("연결실패.....")


def btn_plus(data):
    global angle    
    if (angle+data) >= 180:
        angle = 180
    else:
       angle = angle + data
       
    duty = getDuty(angle)
    print(angle)
    pwm_servo.ChangeDutyCycle(duty)
    print("각도:",angle)
    
    
def btn_minus(data):
    global angle
    if (angle-data) <= 0:
        angle = 0
    else:
        angle = angle - data
    duty = getDuty(angle)
    print(angle)
    pwm_servo.ChangeDutyCycle(duty)
    print("각도:",angle)
            
def on_message(client, userdata, message):
    myval = message.payload.decode("utf-8").split(":")
    #print(message.topic+"-----"+myval)
    if myval[1] =="led_on":
        print("on")
        gpio.output(led_pin,gpio.HIGH)
    elif myval[1] == "led_off":
        print("off")
        gpio.output(led_pin,gpio.LOW)     
    elif myval[0] == "plus":
        print("플러스")
        btn_plus(int(myval[1]))
    elif myval[0] == "minus":
        print("마이너스")    
        btn_minus(int(myval[1]))
        
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
