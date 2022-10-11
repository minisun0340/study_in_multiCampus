import paho.mqtt.publish as publisher

publisher.single("test/server", "cool?!!", hostname="172.30.1.59")