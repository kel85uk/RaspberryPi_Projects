# USAGE
# python track.py --video video/sample.mov

# import the necessary packages
import cv2
import imutils
from imutils.video import VideoStream
import math
import time
import datetime

# initialize the current frame of the video, along with the list of
# ROI points along with whether or not this is input mode
frame = None
roiPts = []
inputMode = False
key = None

def mouseOn(event,x,y,flags,param):
	global key
	if event==cv2.EVENT_LBUTTONDOWN:
		key = ord("q")
	else:
		key = ord("v")
	
#key = None

def main():
	global frame, key
	# initialize the camera and grab a reference to the raw camera capture
	wdth = int(math.floor(360))
	hgth = int(math.floor(800))
	camera = VideoStream(usePiCamera=True,resolution=(wdth,hgth)).start()
	time.sleep(0.5)
	# setup the mouse callback
	cv2.startWindowThread()
	cv2.namedWindow("Detection")
	cv2.setMouseCallback("Detection",mouseOn)
	# keep looping over the frames
	#for frame2 in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	while True:
		frame = camera.read();
		frame = cv2.transpose(frame);
		frame = cv2.flip(frame,1)
		timestamp = datetime.datetime.now()
		ts = timestamp.strftime("%d/%m/%Y %H:%M:%S")
		cv2.putText(frame,ts,(10,frame.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX,0.35,(0,255,0),1)
		cv2.imshow("Detection", frame);
		#cv2.setMouseCallback("Detection",mouseOn)
		#key = cv2.waitKey(10) & 0xFF
		# if the 'q' key is pressed, stop the loop
		if key == ord("q"): #cv2.EVENT_LBUTTONDOWN: #ord("q"):
	#		cv2.destroyAllWindows()
	#		camera.stop()
			break
	# cleanup the camera and close any open windows
	cv2.destroyAllWindows()
	camera.stop()

if __name__ == "__main__":
	main()
