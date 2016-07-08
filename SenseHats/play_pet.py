from sense_hat import SenseHat
import time
import os

sense = SenseHat()

p = [204,0,204]
g = [0, 102, 102]
w = [200, 200, 200]
y = [204, 204, 0]
e = [0,0,0]
r = [255,0,0]
gr = [0,255,0]
bl = [0,0,255]

pet1 = [
    e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    e,g,g,g,g,y,y,e,
    e,g,e,g,e,g,e,e,
    e,e,e,e,e,e,e,e,
    ]

pet2 = [
    e,e,e,e,e,e,e,e,
    p,e,e,e,e,e,e,e,
    e,p,e,e,p,e,p,e,
    e,p,g,g,p,y,y,e,
    e,g,g,g,y,w,y,g,
    e,g,g,g,g,y,y,e,
    e,e,g,e,g,e,e,e,
    e,e,e,e,e,e,e,e,
    ]

iamin = [
    e,e,e,y,y,e,e,e,
    e,e,y,gr,gr,y,e,e,
    e,y,gr,gr,gr,gr,y,e,
    y,gr,gr,gr,gr,gr,gr,y,
    y,gr,gr,gr,gr,gr,gr,y,
    e,y,gr,gr,gr,gr,y,e,
    e,e,y,gr,gr,y,e,e,
    e,e,e,y,y,e,e,e,
    ]
iamout = [
    e,e,e,y,y,e,e,e,
    e,e,y,r,r,y,e,e,
    e,y,r,r,r,r,y,e,
    y,r,r,r,r,r,r,y,
    y,r,r,r,r,r,r,y,
    e,y,r,r,r,r,y,e,
    e,e,y,r,r,y,e,e,
    e,e,e,y,y,e,e,e,
    ]

hostname = '192.168.1.13'

def walking():
	for i in range(10):
		sense.set_pixels(pet1)
		time.sleep(0.5)
		sense.set_pixels(pet2)
		time.sleep(0.5)
def iamin2():
	sense.set_pixels(iamin)
def iamout2():
	sense.set_pixels(iamout)


sense.clear()

x, y, z = sense.get_accelerometer_raw().values()

while(True):
	#x, y, z = sense.get_accelerometer_raw().values()
	#if(x**2+y**2+z**2 > 5):
	response = os.system("sudo ping -c 1 " + hostname)
	if (response <=0):
		iamin2()
#		sense.clear()
	else:
#		walking()
		iamout2()
	time.sleep(60)
	sense.clear()
