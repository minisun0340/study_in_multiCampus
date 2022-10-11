from picamera import PiCamera
from time import sleep

# 사진찍기
camera = PiCamera() # PICamera 객체 생성
# 해상도 적용 - 파이카메라로 최대 해상도는 25XX, 19XX
camera.resolution = (2592, 1944)
camera.framerate = 15 #프레임설정 
camera.start_preview() # 미리보기 화면 시작

#설정은 센서 초기화 전에
camera.rotation = 180 

sleep(10)
camera.capture("/home/pi/mywork/basic/picamera/image.jpg")
camera.stop_preview()