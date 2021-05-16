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
