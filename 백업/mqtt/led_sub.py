import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

led_pin = 21
gpio.setup(led_pin, gpio.OUT)

def connecting(client, userdata, flags, rc):
    print("rc: " + str(rc))
    if rc == 0:
        print("connecting ok")
        client.subscribe("iot/led")
    else:
        print("connecting fail")
        
def message_con(client, userdata, message):
    mymemo = message.payload.decode("utf-8")
    print(message.topic+"------"+mymemo)
    if mymemo == "led_on":
        print("on")
        gpio.output(led_pin, gpio.HIGH)
    else:
        print("off")
        gpio.output(led_pin, gpio.LOW)


try: 
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connecting
    mqttClient.on_message = message_con
    mqttClient.connect("172.30.1.59", 1883, 60)
    mqttClient.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    pass    
    
    
    