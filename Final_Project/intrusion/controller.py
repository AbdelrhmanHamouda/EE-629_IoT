import RPi.GPIO as GPIO
import time
import sys
import requests

GPIO.setmode(GPIO.BCM)
ROOM_SENSOR_PIN = 27
GPIO.setup(ROOM_SENSOR_PIN, GPIO.IN)

def readingRoomSensor():
    if GPIO.input(ROOM_SENSOR_PIN):
        print('motion detected')
        return 1
    else:
        return 0

def runController():
    roomState = readingRoomSensor()
    if roomState == 1:
        setRoomState('yes')
    else:
        setRoomState('no')

def setRoomState(val):
    values = {'name': val}
    r = requests.put('http://127.0.0.1:8000/room/1/', data=values, auth=('pi', '0553156'))

while True:
    try:
        runController()
        time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
