import tkinter
from tkinter import *
top = tkinter.Tk()
var = IntVar()

fancyFrame = Frame(top)
fancyFrame.pack(side = LEFT)

tempFrame = Frame(fancyFrame)
tempFrame.pack(side = TOP)
temp = Label (tempFrame, text="Desired Temperature")
temp.pack(side = TOP)
desiredTemp = Entry(tempFrame, bd =5)
desiredTemp.pack(side = RIGHT)

vibeFrame = Frame(top)
vibeFrame.pack(anchor=CENTER)
vibelabel = Label(vibeFrame, text = "Vibration Setting")
vibelabel.pack(side = TOP)
desiredVibe1 = Radiobutton(vibeFrame, text = "Off", variable=var, value=1)
desiredVibe1.pack(side = BOTTOM)
desiredVibe2 = Radiobutton(vibeFrame, text = "One", variable=var, value=2)
desiredVibe2.pack(side = BOTTOM)
desiredVibe3 = Radiobutton(vibeFrame, text = "Two", variable=var, value=3)
desiredVibe3.pack(side = BOTTOM)

timerFrame = Frame(fancyFrame)
timerFrame.pack(side = BOTTOM)
timer = Label(timerFrame, text = "Timer (Leave blank for no timer)")
timer.pack(side = TOP)
desiredTimer = Entry(timerFrame, bd =5)
desiredTimer.pack(side=BOTTOM)

top.mainloop()
