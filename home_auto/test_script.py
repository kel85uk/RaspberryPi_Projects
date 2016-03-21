import energenie as en
import time
import os
import ephem

o = ephem.Observer()
# Latitude and longitude of the observer (This case it is Delft)
o.lat = '52.0167'
o.long = '4.3667'
s = ephem.Sun()
s.compute()


while True:
	if (os.system("ping -c 1 192.168.1.4")==0)and(time.gmtime().tm_hour>ephem.localtime(o.next_setting(s)).hour)and(time.gmtime().tm_hour<23):
		print "Switch on"
		en.switch_on()
	else:
		print "Switch off"
		en.switch_off()
	time.sleep(30)
	s.compute()
