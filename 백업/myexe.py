from mymqtt1 import mymqttworker
from mymqtt2 import MqttWorker
import time
from mysensor import myPir, myHC, myDht




if __name__=="__main__":
    try: 
        mqttstart = mymqttworker("iot/led")
        mqttstart.working()
        time.sleep(2)
        # pir_test = myPir()
        # pir_test.start()
        dht_test = myDht()
        dht_test.start()
        hc_test=myHC()
        hc_test.start()
    except KeyboardInterrupt:
        pass
    finally:
        print("main end")