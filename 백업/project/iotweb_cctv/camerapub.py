import threading
import picamera
import time
import io

class Mycamera:
    frame = None
    thread = None
    
    def getStreaming(self):
        if Mycamera.thread is None:
            Mycamera.thread = threading.Thread(target=self.streaming)
            Mycamera.thread.start()
            while self.frame is None:
                time.sleep(0)
        return self.frame
            
    @classmethod
    def streaming(c):
        with picamera.PiCamera() as camera:
            camera.resolution = (320,240)
            camera.hflip = True
            camera.vflip = True
            
            camera.start_preview()
            time.sleep(2)
            
            stream = io.BytesIO()
            
            for f in camera.capture_continuous(stream,"jpeg",use_video_port=True):
                stream.seek(0)
                c.frame = stream.read()
                stream.seek(0)
                stream.truncate()
            
            