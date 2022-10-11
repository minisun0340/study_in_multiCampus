import RPi.GPIO as gpio
import paho.mqtt.client as client
import paho.mqtt.publish as publisher
import time

gpio.setmode(gpio.BCM)

myservo = 26
gpio.setup(myservo, gpio.OUT)
pwm = gpio.PWM(myservo, 50)
myangle = 0
pwm.start(3)

def getDuty(degree):
    duty = 2.5 + (degree * (12.5-2.5))/180
    return duty

def connecting(client, userdata, flags, rc):
    if rc == 0:
        print("connecting ok")
        client.subscribe("iot/servo/#")
    else:
        print("connecting fail")
        
def message_con(client, userdata, message):
    global myangle
    mytopic = message.topic
    mymemo = message.payload.decode("utf-8")
    print(message.topic+"------"+mymemo)
    if mytopic == "iot/servo/plus":
        myangle = myangle + int(mymemo)
        print(myangle)
        if myangle >= 180:
            myangle = 180
        myduty = getDuty(myangle)
        pwm.ChangeDutyCycle(myduty)
        time.sleep(1)
        
    elif mytopic == "iot/servo/minus":
        myangle = myangle - int(mymemo)
        print(myangle)
        if myangle <= 0:
            myangle = 0
        myduty = getDuty(myangle)
        pwm.ChangeDutyCycle(myduty)
        time.sleep(1)
        
def send_memo(channel):
        publisher.single("iot/servo/answer", "각입니다", hostname="172.30.1.59")
    
gpio.add_event_detect(myservo, gpio.RISING, callback=send_memo)  
    
try: 
    while True: 
        mqttClient = client.Client()
        mqttClient.on_connect = connecting
        mqttClient.on_message = message_con
        mqttClient.connect("172.30.1.59", 1883, 60)
        mqttClient.loop_forever()
        

    
            
except KeyboardInterrupt:
    pass
finally:
    pass    