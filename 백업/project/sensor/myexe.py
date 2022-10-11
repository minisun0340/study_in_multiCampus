from mymqtt import mymqttworker


if __name__=="__main__":
    try: 
        mmw = mymqttworker()
        mmw.working()
        
    except KeyboardInterrupt:
        pass
    finally:
        pass