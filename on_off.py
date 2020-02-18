#!/usr/bin/python
import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

@app.route('/on', methods=['GET'])
def on():
    GPIO.output(37,1)
    return 'On'

@app.route('/off', methods=['GET'])
def off():
    GPIO.output(37,0)
    return 'Off'
    
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=9080)
