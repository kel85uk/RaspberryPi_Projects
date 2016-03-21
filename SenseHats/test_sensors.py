from sense_hat import SenseHat
from time import sleep
from time import strftime
import os
import matplotlib.pyplot as plt
from drawnow import drawnow


def makeFig():
	plt.plot(timeList,tempList,'o-')
	plt.xlabel('Delta t (sec)')
	plt.ylabel('Temp (C)')

sense = SenseHat()

sense.clear()
sense.low_light = True
plt.ion()

dateList = list()
timeList = list()
tempList = list()

dt = 60
t = 0
fig = plt.figure()
while True:
	#humidity = sense.get_humidity()
	te = os.popen('/opt/vc/bin/vcgencmd measure_temp')
	cputemp = te.read()
	cputemp = cputemp.replace('temp=','')
	cputemp = cputemp.replace('\'C\n','')
	cputemp = float(cputemp)
	temperature = sense.get_temperature_from_pressure()
	temperature = temperature - ((cputemp - temperature)/2)
	t += dt
	pressure = sense.get_pressure()*0.001
	#temp = sense.get_temperature()
	humidity = sense.get_humidity()
	calctemp = temperature #0.0071*temp*temp+0.86*temp-10.0
	calchum = humidity #humidity*(2.5-0.029*temperature)
	stringval1 = " H: %2.1f %%rH" % calchum
	stringval2 = " T: %2.1f C" % calctemp
	stringval3 = " P: %2.3f bar" % pressure
	timestamp = strftime("%d/%m/%Y %H:%M:%S")
	#timestampd = datetime.strptime(str(timestamp),'%d/%m/%Y %H:%M:%S')
	print(timestamp+stringval1)
	print(timestamp+stringval2)
	print(timestamp+stringval3)
	dateList.append(timestamp)
	timeList.append(t)
	tempList.append(calctemp)
	drawnow(makeFig)
	sleep(dt)
