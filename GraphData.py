#Libraries used to create the plots and read in data.
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
rect = fig.patch
f= open("tempCO2.csv","w")
f.write('')#clears file before writing to it
f2= open("tempTVOC.csv","w")
f2.write('')#clears file before writing to it
f3= open("tempTEMP.csv","w")
f3.write('')#clears file before writing to it

#Method that just opens up files where data is being fed into, and graphs them dynamically.
def animate(i):
    fco = 'tempCO2.csv'
    fh = open(fco)
    co = list()
    timeC = list()
    for line in fh:
        pieces = line.split(',')
        degree = pieces[0]
        timeB=  pieces[1]
        timeA= timeB[:8]
        
        time_string = datetime.strptime(timeA,'%H:%M:%S')
        
        
        co.append(float(degree))
        timeC.append(time_string)
        
            
        ax1 = fig.add_subplot(5,1,1)
        
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        ax1.plot(timeC,co,'m')
        plt.title('Current CO2 Level')
        plt.xlabel('Time')
        plt.ylabel('CO2 ppm')

    fTVOC = 'tempTVOC.csv'
    fh2 = open(fTVOC)
    TVOC = list()
    timeC2 = list()
    for line in fh2:
        pieces = line.split(',')
        degree = pieces[0]
        timeB=  pieces[1]
        timeA= timeB[:8]
        
        time_string = datetime.strptime(timeA,'%H:%M:%S')
       
       
        TVOC.append(float(degree))
        timeC2.append(time_string)
        
            
        ax2 = fig.add_subplot(5,1,5)
        
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        ax2.plot(timeC2,TVOC,'c')
        plt.title('Current TVOC Level')
        plt.xlabel('Time')
        plt.ylabel('TVOC')
        
        
    fTEMP = 'tempTEMP.csv'
    fh3 = open(fTEMP)
    TEMP = list()
    timeC3 = list()
    for line in fh3:
        pieces = line.split(',')
        degree = pieces[0]
        timeB=  pieces[1]
        timeA= timeB[:8]
        
        time_string = datetime.strptime(timeA,'%H:%M:%S')
       
        
        TEMP.append(float(degree))
        timeC3.append(time_string)
        
            
        ax3 = fig.add_subplot(5,1,3)
        
        ax3.plot(timeC3,TEMP,'g')
        plt.title('Current Temperature')
        plt.xlabel('Time')
        plt.ylabel('Temperature (C)')
#Define ani and use it to graph plots.
ani = animation.FuncAnimation(fig, animate, interval = 2000)
plt.show()
plt.clf()


