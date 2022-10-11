from picamera import PiCamera
from time import sleep
import paho.mqtt.publish as publisher

camera = PiCamera()
camera.start_preview()
sleep(2)

camera.capture("/home/pi/mywork/basic/picamera/exam1.jpg")
    

file = open("/home/pi/mywork/basic/picamera/exam1.jpg", "rb")
filedata = file.read()
bytefiledata = bytearray(filedata)
print(bytefiledata)

publisher.single("mydata/file", bytefiledata, hostname="172.30.1.59")


camera.stop_preview()