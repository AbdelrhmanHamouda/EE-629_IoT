# Hardware required for this project:
- [PIR sernsor](https://www.adafruit.com/product/189#technical-details)
- Raspberry Pi. This project was implemented on a Pi 4 B. If you have other versions or models, you need to make sure of the IO pins before connecting the hardware in order not to damage your Pi or the sensor
- [Raspberry Pi camera module](https://www.raspberrypi.org/products/camera-module-v2/)
- LED and a resistor in the range of 330 Ω to 1KΩ should work and some female to male wires. **the LED is not necessary, it's just an indication that the sensor is working as it turns on when the sensor detects motion and off when motion is not detected**

# Dependencies and Required Pakcages
```shell
sudo apt-get update 
sudo apt-get upgrade
sudo pip3 install flask
```
# Hardware connection
- The + side of the LED (longer lead) should be connected to GPIO 18, the 6th pin from the left of the top row
- The - side of the LED (shorter lead) should be connected to one side of the resistor
- The other side of the resistor should be connected to ground, the 3rd pin from the left of the top row
- The sensor has three terminals:
  - 5V which should be connected to 1st pin from the left of the top row
  - GND which should be connected to the 3rd pin from the left of the top row
  - Signal or out which should be connected to GPIO 27, the 7th pin from the left of the bottom row

![PIR connection](https://user-images.githubusercontent.com/49162254/118406044-af4ea700-b648-11eb-8b6c-051cc5811f49.jpg)

- The camera module should be connected as shown in the picture below

![connect-camera](https://user-images.githubusercontent.com/49162254/118405175-81676380-b644-11eb-910e-2e9b772d4dcf.gif)

_source: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2_

## Run PIR.py
` python3 PIR.py`

***The server will be running on port `5000` by default. To view the status of the sensor, open a Chromium broweser on Raspberry Pi and go to `0.0.0.0:5000` or on your computer open the browser and type in the address bar `YOUR_RASPBERRY_PI_IP:5000`***
