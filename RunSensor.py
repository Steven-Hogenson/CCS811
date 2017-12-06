#this example reads and prints CO2 equiv. measurement, TVOC measurement, and temp every 2 seconds

from time import sleep
import time
import os
import csv
import sys
from datetime import datetime
from Adafruit_CCS811 import Adafruit_CCS811
csvfile1 = "tempCO2.csv"
csvfile2 = "tempTVOC.csv"
csvfile3 = "tempTEMP.csv"

#f= open("output.txt","w")
ccs =  Adafruit_CCS811()


while not ccs.available():
	pass
temp = ccs.calculateTemperature()

ccs.tempOffset = temp - 25.0
count = 0
while(1):
        co2 = ccs.geteCO2()
	if ccs.available():
            if co2==0:
                co2=400
            #now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	    temp = ccs.calculateTemperature()
	    
	    if not ccs.readData():
              count =0
              #f.write('{}'.format(time.time()))
              #f.write('{}'.format(count))
              #f.write(',')
	      #f.write('{}\n'.format(ccs.geteCO2()))
              #print "CO2: ", ccs.geteCO2(), "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp
              print "CO2: ", co2, "ppm, TVOC: ", ccs.getTVOC(), " temp: ", temp    

	    else:
	      print "ERROR!"
	      while(1):
	      	pass
	    
	timeC = time.strftime("%I")+':'+time.strftime("%M")+':'+time.strftime("%S")
        data1 = [co2, timeC]
        data2 = [ccs.getTVOC(),timeC]
        data3 = [temp,timeC]
        
        with open(csvfile1,"a") as output:
                writer = csv.writer(output,delimiter=",", lineterminator='\n')
                writer.writerow(data1)
                output.flush()
        with open(csvfile2,"a") as output:
                writer = csv.writer(output,delimiter=",", lineterminator='\n')
                writer.writerow(data2)
        with open(csvfile3,"a") as output:
                writer = csv.writer(output,delimiter=",", lineterminator='\n')
                writer.writerow(data3)
	#f.flush()
	time.sleep(5)




