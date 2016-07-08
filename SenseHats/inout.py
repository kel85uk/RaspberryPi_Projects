from sense_hat import SenseHat
import time
import os

sense = SenseHat()

r = [255,0,0]
g = [0,255,0]
b = [0,0,255]
w = [255,255,255]
head = '192.168.1.'
me = 7

def amiinorout(i):
	hostname = head + str(i)
	response = os.system("sudo ping -c 1 -w 1 " + hostname)
	if response <= 0:
		stat = g
#	elif response == 1:
#		stat = b
	else:
		stat = r
	return stat

def fillpixels(k):
	state = []
	for i in range(8):
		for j in range(8):
			if (k):
				state.append(w)
			else:
				address = 1 + j + 8*i
				if address == me:
					state.append(b)
				else:
					amiin = amiinorout(address)
					state.append(amiin)
	return state

def updateSense(state):
	sense.set_pixels(state)

if __name__ == "__main__":
	sense.clear()
	sense.low_light = True
	state = fillpixels(True)
	updateSense(state)
	while(True):
		time.sleep(5)
		state = fillpixels(False)
		updateSense(state)
		
