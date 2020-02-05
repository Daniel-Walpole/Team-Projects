import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("Heating Pad")
#Variables related to GUI
vibeSetting = IntVar()
hours = StringVar()
minutes = StringVar()

#FUNCTIONS
#Fuction printing vibration setting as default, can be changed to send to
#arduino
def getVibeSetting():
    if (vibeSetting.get() != 0):
        print(vibeSetting.get())
        return

#Background Image(Doesn't work?)
background_image = PhotoImage("waves.jpg")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

    
#FRAMES
#Frame that desired temperature and timer are housed in    
fancyFrame = Frame(root, bg = "orange")
fancyFrame.pack(side = LEFT)

#Frame that current Temperature and vibration setting are housed in
specialFrame = Frame(root, bg = "red")
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

#MenuButton for hours
menuHours =  Menubutton(hoursFrame, textvariable = hours)
menuHours.grid()
menuHours.menu =  Menu(menuHours, tearoff = 0 )
menuHours["menu"] = menuHours.menu

#List of Values for hours part of timer
for line1 in range(0, 24):
    menuHours.menu.add_command(label = str(line1), command = hours.set(
        line1))

#Packinging Hour Frame
menuHours.pack(side=LEFT)

#Colon for Timer
colonLabel = Label(timeFrame, text = ":")
colonLabel.pack(side=BOTTOM)

#MenuButton for minutes
menuMinutes =  Menubutton(minutesFrame, textvariable = minutes)
menuMinutes.grid()
menuMinutes.menu =  Menu(menuMinutes, tearoff = 0 )
menuMinutes["menu"] = menuMinutes.menu

#List of Values for hours part of timer
for line2 in range(0, 60):
    menuMinutes.menu.add_command(label = str(line2), command = minutes.set(
        line2))



#Packing Minute Frame    
menuMinutes.pack(side=LEFT)

#Code For Buttons
goButton = Button(buttonFrame, text = "GO!")
stopButton = Button(buttonFrame, text = "STOP!")

goButton.pack(side = LEFT)
stopButton.pack(side = RIGHT)

#End of Code
root.mainloop()
