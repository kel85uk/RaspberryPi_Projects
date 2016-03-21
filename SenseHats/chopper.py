from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()
dt = 0.05
x,y,z = sense.get_accelerometer_raw().values()
while (x**2+y**2+z**2 < 8):
	sense.show_letter("|")
	time.sleep(dt)
        sense.show_letter("/")
	time.sleep(dt)
        sense.show_letter("-")
	x,y,z = sense.get_accelerometer_raw().values()
	time.sleep(dt)
        sense.show_letter("\\")
	time.sleep(dt)
sense.clear()
