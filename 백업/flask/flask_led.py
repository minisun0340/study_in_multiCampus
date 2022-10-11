from typing import final
from flask import Flask, render_template
# 장고의 render = flask에서 reder_template
import RPi.GPIO as gpio
import random

app = Flask(__name__)
led_pin = 21
gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

@app.route("/<command>")
def action(command):
    if command == "on":
        gpio.output(led_pin, gpio.HIGH)
        message = "GPIO"+str(led_pin)+"on"
    elif command == "off":
        gpio.output(led_pin, gpio.LOW)
        message = "GPIO"+str(led_pin)+"off"
    else:
        pass
    
    # resqonse되는 웹페이지에 값을 넘기고 싶은 경우
    msg = {
        "message":message,
        "status":gpio.input(led_pin),
        "hum":random.randrange(40, 50), 
        "temp":random.randrange(20, 25), 
        "distance":random.randrange(20, 100)
    }
    return render_template("led.html", **msg)

if __name__=="__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    except KeyboardInterrupt:
        pass
    finally:
        gpio.cleanup()