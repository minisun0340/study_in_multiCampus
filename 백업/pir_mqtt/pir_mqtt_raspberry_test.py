import RPi.GPIO as gpio
import time
import paho.mqtt.client as pub

pir_pin = 26

gpio.setmode(gpio.BCM)
gpio.setup(pir_pin, gpio.IN)

def pub_ok(client, userdata, mid):
    print(client, userdata, mid)
    print("데이터 전송 ok")

try:
    while True:
        publisher = pub.Client("pir_pub")
        publisher.connect("172.30.1.59", 1883)
        publisher.on_publish = pub_ok

        if gpio.input(pir_pin)==1:
            print("motion detected...")
            result = publisher.publish("pir", "motion detected...")
            print("호출결과: ", result)
        else:
            print("no motion...")
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    gpio.cleanup()