- All credit for the camera streaming files goes to [EbenKouao](https://github.com/EbenKouao). 
- I've done some slight modifications on the index.html file and the main.py to make it work on a differente port
- This project was built using Python3
- This project was built on a Raspberry Pi 4 model B

# Dependencies and Packages Required

```
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install opencv-contrib-python
sudo pip3 install imutils
sudo pip3 install opencv-python
```
# To get it working on your Pi:

## Step 1 Go to camera_stream_flask
`cd EE-629_IoT/camera_stream_flask`

## Step 2 Run the main.py script using Python3
`python3 main.py`

***The server will be running on port 8000 by default. To view the live stream, open a Chromium broweser on Raspberry Pi and go to 0.0.0.0:8000 or on your computer open the browser and type in the address bar <YOUR_RASPBERRY_PI_IP:8000>***

https://user-images.githubusercontent.com/49162254/118404148-98f01d80-b63f-11eb-9087-9c2b5985b943.mp4

