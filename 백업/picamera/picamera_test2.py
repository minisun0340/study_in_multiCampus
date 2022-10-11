from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(10)

for i in range(1, 6):
    sleep(5)
    camera.capture("/home/pi/mywork/basic/picamera/image %d.jpg" % i)

camera.stop_preview()