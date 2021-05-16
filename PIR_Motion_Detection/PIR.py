from flask import Flask, render_template
from flask import send_from_directory
import os
import RPi.GPIO as GPIO
import time
import subprocess
import sys
import requests

GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 27
LED = 18
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def index():
	#while True:
	try:
		
		i = GPIO.input(SENSOR_PIN)
		if i == 0:
			print ("No motion", i)
			GPIO.output(LED, False)
			motion = "not detected"
			time.sleep(3)
		elif i == 1:
			print ("Motion detected", i)
			GPIO.output(LED, True)
			motion = "detected"
			time.sleep(3)
	except KeyboardInterrupt:
		GPIO.cleanup()
		exit()
	return render_template("index.html", motion = motion)
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),
                              	'favicon.ico', 
                              	mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
	app.run(debug = True, port = 5000, host = '0.0.0.0')
