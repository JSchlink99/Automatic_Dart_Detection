from picamera2 import Picamera2
import time
import os
import cv2

# Init camera
camera = Picamera2()

# Set resolution
cam_config = camera.create_still_configuration(main={"format": 'RGB888', "size": (720,480)}, lores={"size": (640,480)},display="lores")
camera.configure(cam_config)
camera.start()
# Init Cv2 window
cv2.namedWindow("Camera")

while True:
	# Capture frame from camera
	frame = camera.capture_array()
	
	# Show the fram in OpenCV window
	cv2.imshow("Camera", frame)
	
	# wait for user input
	key = cv2.waitKey(1) & 0xFF
	
	# If q is pressed, save image and exit loop
	if key == ord('q'):
		score = input("Enter the Score: ")
		number = input("Enter 1/2/3: ")
		count = sum([1 for f in os.listdir("/home/schli/darts/images") if f.startswith(score + "_" + number)])
		filename = os.path.expanduser('~/darts/images/{}_{}_{}.jpg'.format(score,number,count))
		camera.capture_file(filename)
		continue
	# If Z is pressed exit loop
	elif key == ord('z'):
		break
		
cv2.destroyAllWindows()
