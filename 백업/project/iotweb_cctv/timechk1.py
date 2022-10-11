import threading
import time

class timechk1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.count = 0
        
    def run(self):
        pass