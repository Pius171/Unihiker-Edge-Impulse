# Connecting Unihiker to Edge Impulse
**Before moving on, do note that none of the commands below will work if edge-impule-linux is not installed**. Go  to to the root directory of this repository..
Open a terminal on Unihiker and send the command below to connect to Edge Impulse. Make sure a USB camera is attached before sending the command.

```
edge-impulse-linux
```
# About Project
This is an object classification ML model trained to classify LED's based on their color. It is  deployed to DFrobot's Unihiker M10. 
<img width="756" height="538" alt="image" src="https://github.com/user-attachments/assets/64bd09f5-4c5d-434d-ab3e-ceb92731f70f" />

UNIHIKER is a single-board computer that  comes with a 2.8-inch touchscreen display, Wi-Fi, and Bluetooth capabilities. Additionally, it is equipped with a light sensor, accelerometer, gyroscope, and microphone. With its built-in co-processor, UNIHIKER can communicate with a variety of analog/digital/I2C/UART/SPI sensors and actuators. It is based on RK3308 Arm 64-bit 4-core 1.2GHz.

<img width="568" height="360" alt="image" src="https://github.com/user-attachments/assets/4865c023-3bd2-46a5-b5b6-6c6a9bc22827" />

# Data Collection
If the above steps worked well you should now be able to collect data with your camera

# Labelling
During data collection, data is not labelled, so you might have to label each image manually. Draw a bounding box around the object and type in the label name.
<img width="506" height="456" alt="image" src="https://github.com/user-attachments/assets/7a3eeccb-ebcb-4b65-922d-f65b84e498f0" /> <img width="545" height="462" alt="image" src="https://github.com/user-attachments/assets/da6dde66-31b5-4fcc-a498-4bda031f656f" /> <img width="567" height="470" alt="image" src="https://github.com/user-attachments/assets/bc408808-791a-44cf-b633-328c0f26a8bc" /> <img width="571" height="457" alt="image" src="https://github.com/user-attachments/assets/4850bb34-fd6e-466d-a390-7423bf8765dd" />

# Feature Extraction
<img width="572" height="517" alt="image" src="https://github.com/user-attachments/assets/9eb80d5b-92b0-4627-a5f9-2e3ff2f7e006" />
Not so great but my goal here is not accuracy, it is  just to text Unihiker's compability with Edge Impulse.







understand the scope/intricases of the project
show some proof that you actually did the project
expose the tools/skills in between the lines

