# EE-629_IoT
***This is the final project of the EE-629 IoT course***

- The purpose of this project is to detect motion in a room and check the status online in addition to, utilizing a camera live stream to be able to see who brook into your room
- [PIR_Motion_Detection](https://github.com/anasaqeel/EE-629_IoT/tree/main/PIR_Motion_Detection) directory has the instructions on how to set up the PIR sensor and the required Python script
- [camera_stream_flask](https://github.com/anasaqeel/EE-629_IoT/tree/main/camera_stream_flask) directory has the instructions required to set up the camera module and the required Python script
- You will need two terminals to run each script in separate terminal
- Both, the camera and the PIR sensor are implemented using Flask server

## Clone the repo into your directory
`git clone https://github.com/anasaqeel/EE-629_IoT.git`

## In a terminal, go to PIR_Motion_Detection
`cd PIR_Motion_Detection`

## Run PIR.py as mentioned in [PIR_Motion_Detection](https://github.com/anasaqeel/EE-629_IoT/tree/main/PIR_Motion_Detection)
`python3 PIR.py`
### When you open the web page <RASPBERRY_PI_IP:5000> to view the sensor statue, you should see the following:

![no motion](https://user-images.githubusercontent.com/49162254/118405604-d1472a00-b646-11eb-9c62-159f36c92a24.PNG)

                when motion is not detected

![motion detected](https://user-images.githubusercontent.com/49162254/118405627-d60bde00-b646-11eb-9219-1361ce2efc95.PNG)

                when motion is detected

## In another terminal windo, go to camera_stream_flask
`cd camera_stream_flask`
## Run main.py as mentioned in [camera_stream_flask](https://github.com/anasaqeel/EE-629_IoT/tree/main/camera_stream_flask)

### You should be able to see a live stream of the camera on port 8000 when you open the web page <RASPBERRY_PI_IP:8000>
