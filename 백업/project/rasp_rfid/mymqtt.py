import paho.mqtt.client as mqtt

class Mqtt:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.connect
        self.client.on_message = self.message
        self.client.connect("172.30.1.58",1883)
        self.client.loop_forever()
        
    def connect(self, client, userdata, flags, rc):
        print("connect..."+str(rc))
        if rc==0:
            client.subscribe("pi/#")
        else:
            print("연결실패...")
    
    def message(self, client, userdata, message):
        value = message.payload.decode("utf-8")
        print(value)