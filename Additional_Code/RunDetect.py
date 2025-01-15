import time
import torch
from torchvision import transforms
from torchvision import models
from PIL import Image
from picamera2 import Picamera2
import numpy as np
import io
import cv2
import os
import subprocess
import shutil

# Init Camera
camera = Picamera2()

# Load trained yolov5s model
#model = torch.load("yolov5/yolov5s.pt", map_location=torch.device('cpu'))

# Set Resolution
cam_config = camera.create_still_configuration(main={"format": 'RGB888', "size": (720,480)}, lores={"size": (720,480)},display="lores")
camera.configure(cam_config)
camera.start()
# Init Cv2 Window
cv2.namedWindow("Darts")



cmd = f"python yolov5/detect.py --source temp.jpg --weights yolov5/runs/train/yolo_darts_det2/weights/best.pt --conf 0.25 --name output"

while True:
	# Capture frame from camera
	frame = camera.capture_array()
	# Show the frame in OpenCV window
	cv2.imshow("Darts",frame)

	# wait for user input
	key = cv2.waitKey(1) & 0xFF
	
	# If q is pressed continue
	if key == ord('q'):
		start_time = time.time()
		filename = "temp.jpg"
		camera.capture_file(filename)
		print(f"{filename} saved")
		os.system(cmd)
		out_dir = "darts_det"

		# Find highest existing output file number
		existing_files = [f for f in os.listdir(out_dir) if os.path.isfile(os.path.join(out_dir,f)) and f.endswith(".jpg")]
		existing_nums = [int(f[len("output"):-4]) for f in existing_files if f.startswith("output") and f[:-4].lstrip("output").isdigit()]

		if existing_nums:
			new_num = max(existing_nums) + 1
		else:
			new_num = 1

		out_filename = f"output{new_num}.jpg"
		print(f"Moving file {out_filename} to /darts_det")	
		# Move output file to new location
		shutil.move("yolov5/runs/detect/output/temp.jpg", f"darts_det/{out_filename}")
		image = cv2.imread(f"darts_det/{out_filename}")
		cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
		cv2.imshow('Image',image)
		# Delete output directory
		if os.path.exists("yolov5/runs/detect/output"):
			os.rmdir("yolov5/runs/detect/output")
			print(f"yolov5/runs/detect/output/temp.jpg saved")
		else:
			print(f"yolov5/runs/detect/output does not exist")
		end_time = time.time()
		elapsed_time = end_time - start_time
		print(f"Elapsed time: {elapsed_time:.2f} seconds")
		continue
	# If z is pressed stop
	elif key == ord('z'):
		break
		
cv2.destroyAllWindows()
