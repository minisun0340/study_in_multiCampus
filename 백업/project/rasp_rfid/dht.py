from threading import Thread
import paho.mqtt.publish as publish
import time
import board # 데이터 송신용 board모듈
import adafruit_dht

humidFileRoute = "/home/pi/iot/humid.json"
tempFileRoute = "/home/pi/iot/temp.json"

class SEN(Thread):
    def __init__(self, file):
        super().__init__()
        self.mydht11 = adafruit_dht.DHT11(board.D12)
        self.file = file
        self.humid = self.file.jsonfile(humidFileRoute)
        self.temp = self.file.jsonfile(tempFileRoute)
        
    def run(self):
        while True:
            try:
                humidity_data = self.mydht11.humidity
                temperature_data = self.mydht11.temperature
                publish.single("android/dht",
                "hu:"+str(humidity_data)+":"+str(temperature_data),hostname="172.30.1.58")
                print(humidity_data, temperature_data)
                self.file.dht_save(humidity_data, humidFileRoute, self.humid)
                self.file.dht_save(temperature_data, tempFileRoute, self.temp)
                time.sleep(3)
            except RuntimeError as error:
                print(error.args[0])
            finally:
                pass