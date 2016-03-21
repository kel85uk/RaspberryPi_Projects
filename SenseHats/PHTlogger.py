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
finetempList = np.array([])
finepresList = np.array([])
finerHList = np.array([])

dateFile = open('Datefiles.log','w')
tempFile = open('Tempfiles.log','w')
presFile = open('Presfiles.log','w')
humiFile = open('Humifiles.log','w')

dt = 60
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
	
	if (t%dt==0):
		dateList.append(timestamp)
		timeList.append(t)
		tempList.append(np.mean(finetempList))
		presList.append(np.mean(finepresList))
		rHList.append(np.mean(finerHList))
		dateFile.write(str(timestamp) + '\n')
		tempFile.write(str(finetempList.mean()) + '\n')
		presFile.write(str(finepresList.mean()) + '\n')
		humiFile.write(str(finerHList.mean()) + '\n')
		dateFile.flush()
		tempFile.flush()
		presFile.flush()
		humiFile.flush()
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
		finetempList = np.array([])
		finepresList = np.array([])
		finerHList = np.array([])
	sleep(1)
