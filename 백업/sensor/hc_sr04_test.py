from tkinter import E
from turtle import distance
import RPi.GPIO as gpio
import time

TRIGER = 5
ECHO = 6

gpio.setmode(gpio.BCM)
gpio.setup(TRIGER, gpio.OUT)
gpio.setup(ECHO, gpio.IN)

def getDistance():
    gpio.output(TRIGER, False)
    time.sleep(1)
    gpio.output(TRIGER, True)
    time.sleep(0.00001) #마이크로세컨드는 백만분의 1초(0.000001) 10ms이므로 10 곱함
    gpio.output(TRIGER, False)
    
    while gpio.input(ECHO) == 0 :
        pulse_start = time.time() #현재 시간을 측정 - High신호가 발생되는 시간을 측정
        
    while gpio.input(ECHO) == 1:
        pulse_end = time.time() #ECHO핀이 LOW신호가 발생되는 시간을 측정
        
    pulse_duration = pulse_end - pulse_start
    
    distance = pulse_duration * 340 * 100 /2
    distance = round(distance, 2)
    return distance

if __name__=="__main__":
    try:
        while True:
            distance_value = getDistance()
            if 4<distance_value<400:
                print("distance: % .2f cm" % distance_value)
            else:
                print("범위가 벗어남")
    except KeyboardInterrupt:
        pass
    finally:
        gpio.cleanup()