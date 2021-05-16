# Hardware required for this project:
- [PIR sernsor](https://www.adafruit.com/product/189#technical-details)
- Raspberry Pi. This project was implemented on a Pi 4 B. If you have other versions or models, you need to make sure of the IO pins before connecting the hardware in order not to damage your Pi or the sensor
- [Raspberry Pi camera module](https://www.raspberrypi.org/products/camera-module-v2/)
- LED and a resistor in the range of 330 Ω to 1KΩ should work and some female to male wires. **the LED is not necessary, it's just an indication that the sensor is working as it turns on when the sensor detects motion and off when motion is not detected**

# Dependencies and Required Pakcages
```
sudo apt-get update 
sudo apt-get upgrade
sudo pip3 install flask
```
## Run PIR.py
` python3 PIR.py`

***The server will be running on port 5000 by default. To view the status of the sensor, open a Chromium broweser on Raspberry Pi and go to 0.0.0.0:5000 or on your computer open the browser and type in the address bar <YOUR_RASPBERRY_PI_IP:5000>
