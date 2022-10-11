import threading
import picamera
import time
import io

class MyCamera:
    frame = None #공유변수. self가 붙으면 인스턴스변수
    thread = None
    # streaming메소드를 쓰레드로 동작시키며 스트리밍되는 frame을 외부로 보내는 메소드
    def getStreaming(self):
        if MyCamera.thread is None:
            MyCamera.thread = threading.Thread(target=self.streaming)
            MyCamera.thread.start()
            while self.frame is None: # 이 코드가 없으면 프레임이 없는 상태가 넘어감. 프레임이 없으면 넘기지 않도록 잡아줌
                time.sleep(0) # 쓰레드 계속 실행하기
        return self.frame
    
    @classmethod #- 클래스 명 넣어주기  MyCamera클래스를 c에 저장
    def streaming(c):
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240) #해상도
            camera.hflip = True #수직 수평 뒤집기
            camera.vflip = True
            
            camera.start_preview()
            time.sleep(2)
            
            stream = io.BytesIO()   #메모리상 갖고 있는 바이트스트림
            for f in camera.capture_continuous(stream, "jpeg", use_video_port=True):
                stream.seek(0)
                c.frame = stream.read()
                # 다음캡쳐를 위한 준비 - 파일의 내용을 비우기
                stream.seek(0)
                stream.truncate()