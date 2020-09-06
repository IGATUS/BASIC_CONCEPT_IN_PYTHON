from tkinter import *
import sys
import time
root = Tk()
label=Label(root,text='Digital Clock',font=('times 35 bold'))
label.grid(row=0,column=2)
l2=Label(root,font=('times 50 bold'),bg='skyblue')
l2.grid(row=2,column=2)
calib=Label(root,text='Hours  Minutes  Seconds',font=('times 20 bold'))
calib.grid(row=4,column=2)
def myTime():
    curT=time.strftime('%H:%M:%S')
    l2.config(text=curT)
    l2.after(200,myTime)
myTime()
root.mainloop()