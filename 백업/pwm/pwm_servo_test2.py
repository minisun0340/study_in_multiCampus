import RPi.GPIO as gpio
import time

servo_pin = 19
gpio.setmode(gpio.BCM)
gpio.setup(servo_pin, gpio.OUT)
pwm = gpio.PWM(servo_pin, 50) # 반드시 50Hz 로 정해짐
pwm.start(3) # 서보모터의 초기값을 0으로 설정(듀티비 2.5 = 0도, 듀티비 7.5는 90도, 듀티비 12.5는 180도)
for i in range(3, 13): #range(30, 125)
    pwm.ChangeDutyCycle(i) #i/10 로 주면 조금 더 정밀하게 나타남
    time.sleep(0.02)


pwm.ChangeDutyCycle(3)
time.sleep(2)
pwm.stop()
gpio.cleanup()