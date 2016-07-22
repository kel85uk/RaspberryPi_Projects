from sense_hat import SenseHat
from time import sleep
from time import strftime
import numpy as np
import os
import matplotlib.pyplot as plt

sense = SenseHat()

sense.clear()
sense.low_light = True
plt.ion()

dateList = list()
timeList = list()
tempList = list()
presList = list()
rHList	 = list()
xList = list()
yList = list()
zList = list()
finetempList = np.array([])
finepresList = np.array([])
finerHList = np.array([])
finexList = np.array([])
fineyList = np.array([])
finezList = np.array([])

dateFile = open('Datefiles.log','w')
tempFile = open('Tempfiles.log','w')
presFile = open('Presfiles.log','w')
humiFile = open('Humifiles.log','w')
xFile = open('x_files.log','w')
yFile = open('y_file.log','w')
zFile = open('z_file.log','w')

dt = 2
t = 0
#fig = plt.figure()
#ax1 = fig.add_subplot(3,1,1)
#ax2 = fig.add_subplot(3,1,2)
#ax3 = fig.add_subplot(3,1,3)
while True:
	#humidity = sense.get_humidity()
	te = os.popen('/opt/vc/bin/vcgencmd measure_temp')
	cputemp = te.read()
	cputemp = cputemp.replace('temp=','')
	cputemp = cputemp.replace('\'C\n','')
	cputemp = float(cputemp)
	temperature = sense.get_temperature_from_pressure()
	temperature = temperature - ((cputemp - temperature)/2)
	t += 1
	pressure = sense.get_pressure()*0.001
	#temp = sense.get_temperature()
	humidity = sense.get_humidity()
	calctemp = temperature #0.0071*temp*temp+0.86*temp-10.0
	calchum = humidity #humidity*(2.5-0.029*temperature)
	stringval1 = " H: %2.1f %%rH" % calchum
	stringval2 = " T: %2.1f C" % calctemp
	stringval3 = " P: %2.3f bar" % pressure
	timestamp = strftime("%d/%m/%Y %H:%M:%S")
	print(timestamp+stringval1)
	print(timestamp+stringval2)
	print(timestamp+stringval3)
	finetempList = np.append(finetempList,calctemp)
	finepresList = np.append(finepresList,pressure)
	finerHList = np.append(finerHList,humidity)
	x,y,z = sense.get_accelerometer_raw().values()
	finexList = np.append(finexList,x)
	fineyList = np.append(fineyList,y)
	finezList = np.append(finezList,z)
	#print x,y,z
	if (t%dt==0):
		dateList.append(timestamp)
		timeList.append(t)
		tempList.append(np.mean(finetempList))
		presList.append(np.mean(finepresList))
		rHList.append(np.mean(finerHList))
		xList.append(np.mean(finexList))
		yList.append(np.mean(fineyList))
		zList.append(np.mean(finezList))
		dateFile.write(str(timestamp) + '\n')
		tempFile.write(str(finetempList.mean()) + '\n')
		presFile.write(str(finepresList.mean()) + '\n')
		humiFile.write(str(finerHList.mean()) + '\n')
		xFile.write(str(finexList.mean()) + '\n')
		yFile.write(str(fineyList.mean()) + '\n')
		zFile.write(str(finezList.mean()) + '\n')
		dateFile.flush()
		tempFile.flush()
		presFile.flush()
		humiFile.flush()
		xFile.flush()
		yFile.flush()
		zFile.flush()
		#ax1.clear()
		#ax2.clear()
		#ax3.clear()
		#ax1.plot(timeList,tempList,'ro-')
		#ax1.set_ylabel('Temp (C)')
		#ax2.plot(timeList,presList,'bo-')
		#ax2.set_ylabel('Pressure (bar)')
		#ax3.plot(timeList,rHList,'go-')
		#ax3.set_ylabel('RH (%)')
		#fig.canvas.draw()
		del finetempList
		del finepresList
		del finerHList
		del finexList
		del fineyList
		del finezList
		finetempList = np.array([])
		finepresList = np.array([])
		finerHList = np.array([])
		finexList = np.array([])
		fineyList = np.array([])
		finezList = np.array([])
	sleep(1)
