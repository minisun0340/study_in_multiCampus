from picamera import PiCamera, Color
from time import sleep

# 사진찍기
camera = PiCamera()
camera.start_preview() 
camera.annotate_text = "raspberry PI" # 사진에 글쓰기
camera.annotate_text_size = 50
camera.annotate_background = Color("blue")
camera.annotate_foreground = Color("yellow")

sleep(10)
camera.capture("/home/pi/mywork/basic/picamera/image6.jpg")
camera.stop_preview()