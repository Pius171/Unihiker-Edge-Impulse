# GESTURE RECOGNITION
A gesture recognition system that uses Unihiker's inbuilt acceleromter to detect the following gestures

* up-down motion
* left-right motion
* idle

## Tools needed
* Unihiker
* Edge Impulse
* USB-C Cable

## Data Collection
Open data_collection.py, set the label name to the label you want to collect data for and run the code. Hold down button A to start collecting data, when you release button A data collection stops, when you hold button A again data collection continues. Press Button B when done with data collection to export the data into a zip file. Each sample is a separate csv file, as per edge impulse requirement. Repeat this for other labels.

## Train on edge impulse
Upload data to edge impulse and train

### Trainning Results
<img width="609" height="669" alt="image" src="https://github.com/user-attachments/assets/1f120a5c-85f6-4d85-a484-a02eaac95930" />
<img width="598" height="530" alt="image" src="https://github.com/user-attachments/assets/0c105dbd-fc9a-48b9-9457-f3ce939d98cb" />

### Test results
<img width="603" height="677" alt="image" src="https://github.com/user-attachments/assets/a85f4a13-cb86-4b5b-bf19-d557bd82a7aa" />

### Life inferencing
![predictionvideoedited-ezgif com-optimize](https://github.com/user-attachments/assets/a5d6f07b-c830-4ebc-82f9-0f50ea4677a8)



You can find the edge impulse project at this [link](https://studio.edgeimpulse.com/public/752659/live)



value
