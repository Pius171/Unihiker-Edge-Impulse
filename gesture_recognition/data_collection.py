#data is collected and stored in a pandas dataframe
#each row in the dataframe is converted to a separate CSV file
#This is how Edge Impulse wants the data
import time
import pandas as pd
from pinpong.board import *
from pinpong.extension.unihiker import *
import os
import zipfile

# Initialize UniHiker
Board().begin()

# Create data directory if it doesn't exist
label="circular"
output_dir = "/root/my_codes/{}_samples".format(label)
zip_output_path = "/root/my_codes/{}_samples.zip".format(label)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize empty list to store data
data = []
sample_count = 0

print("Ready to collect motion data. Press A to collect, B to stop and export")

while True:
    # Read motion data
    ax = accelerometer.get_x()
    ay = accelerometer.get_y()
    az = accelerometer.get_z()
    strength = accelerometer.get_strength()
    gx = gyroscope.get_x()
    gy = gyroscope.get_y()
    gz = gyroscope.get_z()
    timestamp = time.time()

    # Collect sample if A is pressed
    if button_a.is_pressed():
        sample_count += 1
        if sample_count <= 500:
            data.append({
                "timestamp": timestamp,
                "acc_x": ax,
                "acc_y": ay,
                "acc_z": az,
                "acc_strength": strength,
                "gyro_x": gx,
                "gyro_y": gy,
                "gyro_z": gz
            })
            print(f"[{label}] Sample {sample_count} recorded.")
        else:
            print("Maximum sample count (500) reached.")
            buzzer.play(buzzer.DADADADUM, buzzer.Once)  # Play music once

    # Exit and export if B is pressed
    if button_b.is_pressed():
        print("Exporting samples as individual CSV files...")

        df = pd.DataFrame(data)

        for i, row in df.iterrows():
            single_df = pd.DataFrame([row])  # convert row to DataFrame
            file_name = f"{label}_{i+1:03}.csv"  # e.g., idle_001.csv
            file_path = os.path.join(output_dir, file_name)
            single_df.to_csv(file_path, index=False)
            print(f"Saved: {file_path}")

        print(f"Export complete. {len(df)} samples saved.")

        # Zip the output folder
        print("Creating ZIP archive...")
        with zipfile.ZipFile(zip_output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, os.path.dirname(output_dir))
                    zipf.write(full_path, relative_path)
        print(f"ZIP archive created at: {zip_output_path}")
        break

    time.sleep(0.1)
