import time
import numpy as np
import tflite_runtime.interpreter as tflite
from pinpong.board import Board
from pinpong.extension.unihiker import *
from unihiker import GUI   #import pack

gui = GUI()  #Instantiate GUI class

# Initialize UniHiker
Board().begin()

# Load TFLite model
model_path = "/root/my_codes/ML/ei-ml-pipleline-classifier-tensorflow-lite-float32-model.3.lite"
interpreter = tflite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Rolling window to hold 100 samples of 7 features each
window = []

# Labels (edit based on your Edge Impulse project)
labels = ["circular","idle","left-right","up-down"]  # replace with actual labels

print("Starting live inference... Press B to stop.")

while True:
    # Read data from sensors
    ax = accelerometer.get_x()
    ay = accelerometer.get_y()
    az = accelerometer.get_z()
    strength = accelerometer.get_strength()
    gx = gyroscope.get_x()
    gy = gyroscope.get_y()
    gz = gyroscope.get_z()

    # Append current reading to window
    window.append([ax, ay, az, strength, gx, gy, gz])

    # Maintain only 100 latest samples
    if len(window) > 100:
        window.pop(0)

    # Once window is filled, perform inference
    if len(window) == 100:
        # Example: Taking the latest single sample from the window
        latest_sample = window[-1] # Get the last sample from the window

# Reshape the sample to match the model's expected input shape [1 7]
        input_data = np.array(latest_sample, dtype=np.float32).reshape(1, 7)
        #input_data = np.array(window, dtype=np.float32).reshape(1,7)
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        output = interpreter.get_tensor(output_details[0]['index'])

        predicted_index = np.argmax(output)
        predicted_label = labels[predicted_index]
        confidence = output[0][predicted_index]

        # Display result on screen
        print(f"Prediction: {predicted_label} ({confidence*100:.2f}%)")
        #display.show(predicted_label)
        gui.draw_text(x = 120,y=160,text=predicted_label,origin='left' )
        gui.clear()

    # Exit if B is pressed
    if button_b.is_pressed():
        print("Stopping inference.")
        break

    time.sleep(0.05)  # 50 ms sampling rate
