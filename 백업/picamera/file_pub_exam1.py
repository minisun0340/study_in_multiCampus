from picamera import PiCamera
from time import sleep
import paho.mqtt.publish as publisher

camera = PiCamera()
camera.start_preview()
sleep(2)

for i in range(1, 6):
    sleep(2)
    camera.capture("/home/pi/mywork/basic/picamera/exam%s.jpg" % i)
    file = open("/home/pi/mywork/basic/picamera/exam%s.jpg" % i, "rb")
    filedata = file.read()
    bytefiledata = bytearray(filedata)
    print(bytefiledata)
    publisher.single("mydata/file", bytefiledata, hostname="172.30.1.59")
    
camera.stop_preview()