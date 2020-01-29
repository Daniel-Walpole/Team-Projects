import tkinter
from tkinter import *
root = tkinter.Tk()
#Variables related to GUI
vibeSetting = IntVar()

#Printing Vibration setting as default, can be changed to send to arduino
def getVibeSetting():
    if (vibeSetting.get() != 0):
        print(vibeSetting.get())
        return

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
desiredTemp = Spinbox(tempFrame, from_ = 98, to = 169)
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
desiredVibe1 = Radiobutton(vibeFrame, text = "Off", variable=vibeSetting, value=0,
                           command = getVibeSetting)
desiredVibe1.pack(side = BOTTOM)
desiredVibe2 = Radiobutton(vibeFrame, text = "One", variable=vibeSetting, value=1,
                           command = getVibeSetting)
desiredVibe2.pack(side = BOTTOM)
desiredVibe3 = Radiobutton(vibeFrame, text = "Two", variable=vibeSetting, value=2,
                           command = getVibeSetting)
desiredVibe3.pack(side = BOTTOM)

#Code for Timer
#Frames
timerFrame = Frame(fancyFrame)
timerFrame.pack(side = BOTTOM)
timerLabel = Label(timerFrame, text = "Timer (Leave blank for no timer)")
timerLabel.pack(side = TOP)

timeFrame = Frame(timerFrame)
timeFrame.pack(side = BOTTOM)

hoursFrame = Frame(timeFrame)
hoursFrame.pack(side = LEFT)

minutesFrame = Frame(timeFrame)
minutesFrame.pack(side = RIGHT)

#Colon for Timer(Doesn't work for some reason?
#colonLabel = Label(timeFrame, text = ":")

#Scrollbar for hours
scrollbarHours = Scrollbar(hoursFrame)
scrollbarHours.pack(side = RIGHT, fill = Y)

#List of Values for hours part of timer
timeHours = Listbox(hoursFrame, yscrollcommand = scrollbarHours.set)
for line1 in range(0, 24):
    timeHours.insert(END, str(line1))

#Packinging Hour Frame
timeHours.pack(side=LEFT, fill = BOTH)
scrollbarHours.config(command = timeHours.yview)

#Scrollbar for minutes
scrollbarMinutes = Scrollbar(minutesFrame)
scrollbarMinutes.pack(side = RIGHT, fill = Y)

#List of Values for minutes part of timer
timeMinutes = Listbox(minutesFrame, yscrollcommand = scrollbarMinutes.set)
for line2 in range(0, 59):
    timeMinutes.insert(END, str(line2))

#Packing Minute Frame    
timeMinutes.pack(side=LEFT, fill = BOTH)
scrollbarMinutes.config(command = timeMinutes.yview)


#Code For Buttons
goButton = Button(buttonFrame, text = "GO!")
stopButton = Button(buttonFrame, text = "STOP!")

goButton.pack(side = LEFT)
stopButton.pack(side = RIGHT)

#End of Code
root.mainloop()
