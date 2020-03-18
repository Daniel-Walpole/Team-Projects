import tkinter
import time
from tkinter import *
import math
root = tkinter.Tk()
root.title("Heating Pad")
#Variables related to GUI
vibeSetting = IntVar()
t0 = 0

#FUNCTIONS
#Truncate function found online
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

#Fuction printing vibration setting as default, can be changed to send to
#arduino
def getVibeSetting():
        print(vibeSetting.get())
        return

#GO button function
def getValues():
    global t0
    t0 = time.time()
    if (int(desiredTemp.get()) >= 100):
        print("1" + str(desiredTemp.get()) + "000" + str(vibeSetting.get())
          + str(hours.get()) + str(minutes.get()) + "00")
    else:
        print("1" + "0" + str(desiredTemp.get()) + "000" + str(vibeSetting.get())
          + str(hours.get()) + str(minutes.get()) + "00")
    return

#STOP button function
def stop():
    t1 = time.time()
    global t0
    totalTime = t1 - t0
    totalTime = truncate(totalTime, 2) #remove this line if you want all decimals
    print("00000000000000")
    file = open('time.py', 'w')
    file.write("Start Time: " + str(t0) + '\n')
    file.write("End Time: " + str(t1) + '\n')
    file.write("Total time: " + str(totalTime) + '\n')
    file.close()
    return

#Background Image(Doesn't work?)
background_image = PhotoImage("waves.jpg")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

    
#FRAMES
#Frame that desired temperature and timer are housed in    
fancyFrame = Frame(root)
fancyFrame.pack(side = LEFT)

#Frame that current Temperature and vibration setting are housed in
specialFrame = Frame(root)
specialFrame.pack(side = RIGHT)

#Frame that the Buttons are housed int
buttonFrame = Frame(root)
buttonFrame.pack(side = BOTTOM)

#Frame related to all temperature widgets
tempFrame = Frame(fancyFrame)
tempFrame.pack(side = TOP)

#Code for Desired temperature related widgets
desiredTempLabel = Label (tempFrame, text="Desired Temperature(°F)")
desiredTempLabel.pack(side = TOP)
desiredTemp = Spinbox(tempFrame, from_ = 98, to = 169, state= 'readonly')
desiredTemp.pack(side = BOTTOM)

#Code for Current Temperature related Widgets
currentTempFrame = Frame(specialFrame)
currentTempFrame.pack(side = TOP)

currentTempLabel = Label(currentTempFrame, text = "Current Temperature:")
currentTemp = Label(currentTempFrame, text = "98")

currentTempLabel.pack(side= TOP)
currentTemp.pack(side= BOTTOM)

#Code for Vibration Settings
vibeFrame = Frame(specialFrame)
vibeFrame.pack(side = BOTTOM)

vibeLabel = Label(vibeFrame, text = "Vibration Setting")
vibeLabel.pack(side = TOP)

desiredVibeOff = Radiobutton(vibeFrame, text = "Off", variable=vibeSetting,
                           value=0)
desiredVibeOff.pack(side = BOTTOM)

desiredVibe1 = Radiobutton(vibeFrame, text = "One", variable=vibeSetting,
                           value=1)
desiredVibe1.pack(side = BOTTOM)

desiredVibe2 = Radiobutton(vibeFrame, text = "Two", variable=vibeSetting,
                           value=2)
desiredVibe2.pack(side = BOTTOM)

desiredVibe3 = Radiobutton(vibeFrame, text = "Three", variable=vibeSetting,
                           value=3)
desiredVibe3.pack(side = BOTTOM)

#Code for Timer
#Frames
timerFrame = Frame(fancyFrame)
timerFrame.pack(side = BOTTOM)
timerLabel = Label(timerFrame, text = "Timer (Leave blank for no timer)\nHours\tMinutes")
timerLabel.pack(side = TOP)

timeFrame = Frame(timerFrame)
timeFrame.pack(side = BOTTOM)

hoursFrame = Frame(timeFrame)
hoursFrame.pack(side = LEFT)

minutesFrame = Frame(timeFrame)
minutesFrame.pack(side = RIGHT)

#OptionMenu for hours
hours = StringVar(hoursFrame)
hours.set('00')

hoursChoices = ["00", "01", "02", "03","04", "05", "06", "07",
                "08", "09", "10", "11", "12", "13", "14", "15",
                "16", "17", "18", "19", "20", "21", "22", "23"]
hoursMenu = OptionMenu(hoursFrame, hours, *hoursChoices)

#Packinging Hours Menu
hoursMenu.pack(side=LEFT)

#Colon for Timer
colonLabel = Label(timeFrame, text = ":")
colonLabel.pack(side=BOTTOM)

#OptionMenu for minutes

minutes = StringVar(minutesFrame)
minutes.set('00')

minutesChoices = ["00", "01", "02", "03","04", "05", "06", "07",
                "08", "09", "10", "11", "12", "13", "14", "15",
                "16", "17", "18", "19", "20", "21", "22", "23",
                "24", "25", "26", "27", "28", "29", "30", "31",
                "32", "33", "34", "35", "36", "37", "38", "39",
                "40", "41", "42", "43", "44", "45", "46", "47",
                "48", "49", "50", "51", "52", "53", "54", "55",
                "56", "57", "58", "59"]
minutesMenu = OptionMenu(minutesFrame, minutes, *minutesChoices)

#Packinging Minutes Menu
minutesMenu.pack(side=LEFT)

#Code For Buttons(add a command by setting command = functionnamehere(parameters))
goButton = Button(buttonFrame, text = "GO!", command = getValues)
stopButton = Button(buttonFrame, text = "STOP!", command = stop)

goButton.pack(side = LEFT)
stopButton.pack(side = RIGHT)

#End of Code
root.mainloop()
