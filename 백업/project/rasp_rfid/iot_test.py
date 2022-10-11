from mymqtt_camera_rfid import mymqttworker
if __name__ == "__main__":
    try:
        camera = mymqttworker()
        camera.working()
    except KeyboardInterrupt:
        pass
    finally:
        pass