from picamera import PiCamera
from time import sleep

# 사진찍기
camera = PiCamera() # PICamera 객체 생성
camera.start_preview() # 미리보기 화면 시작
# 동영상 저장 시작

camera.start_recording("/home/pi/mywork/basic/picamera/video.h264")
# 카메라의 센서가 빛의 수준을 감지 할 시간이 있어야 하므로 이미지를 캡쳐하기 전에 최소 2초는 sleep
sleep(10)
camera.stop_recording()
camera.stop_preview()