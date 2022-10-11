import RPi.GPIO as gpio
import time
import paho.mqtt.publish as publisher

servo_pin = 22
gpio.setmode(gpio.BCM)
gpio.setup(servo_pin, gpio.OUT)
pwm = gpio.PWM(servo_pin, 50) # 반드시 50Hz 로 정해짐
pwm.start(3) # 서보모터의 초기값을 0으로 설정(듀티비 2.5 = 0도, 듀티비 7.5는 90도, 듀티비 12.5는 180도)

try:
    for i in range(30, 125, 10): #range(30, 125)
        pwm.ChangeDutyCycle(i/10) #i/10 로 주면 조금 더 정밀하게 나타남
        time.sleep(1)
        print(i)
        publisher.single("iot/servo", str(i), hostname="172.30.1.59")
        
    pwm.ChangeDutyCycle(3)
    time.sleep(2)
    pwm.ChangeDutyCycle(0)
finally:
    pwm.stop()
    gpio.cleanup()