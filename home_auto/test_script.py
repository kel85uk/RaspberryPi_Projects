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
UTC_offset = 1 # Can always switch to daylight check
sleep_hour = 23
wake_hour = 7


while True:
	current_hour = time.gmtime().tm_hour + UTC_offset
	sunset_hour = ephem.localtime(o.next_setting(s)).hour + UTC_offset
	daylight_hour = (ephem.localtime(o.next_rising(s)).hour + 1) + UTC_offset # Give an extra hour for daylight
	condition1 = (os.system("ping -c 1 192.168.1.4")==0)
	condition2 = (current_hour>sunset_hour)or(current_hour<sleep_hour)
	condition3 = (current_hour>wake_hour)or(current_hour<daylight_hour)
	if condition1 and (condition2 or condition3):
		print "Switch on"
		#en.switch_on()
	else:
		print "Switch off"
		#en.switch_off()
	time.sleep(30)
	s.compute()
