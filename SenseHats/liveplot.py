from time import sleep
import numpy as np
import matplotlib.pyplot as plt

dt = 30
plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
while(True):
	tempList = np.genfromtxt("Tempfiles.log",delimiter="\n")
	presList = np.genfromtxt("Presfiles.log",delimiter="\n")
	rHList = np.genfromtxt("Humifiles.log",delimiter="\n")
	timeList = np.linspace(0,60*len(tempList),len(tempList))
	sleep(dt)
	ax1.clear()
	ax2.clear()
	ax3.clear()
	ax1.plot(timeList,tempList,'ro-')
	ax1.set_ylabel('Temp (C)')
	ax2.plot(timeList,presList,'bo-')
	ax2.set_ylabel('Pressure (bar)')
	ax3.plot(timeList,rHList,'go-')
	ax3.set_ylabel('RH (%)')
	fig.canvas.draw()
	#sleep(dt)
