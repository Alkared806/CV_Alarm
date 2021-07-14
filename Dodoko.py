from tkinter import *
import time as t
from Budilnik import BLUD
from TEST import video

dc=Tk()
frame_b = Frame()
dc.title ("CLOCK")
dc.geometry ("400x100")

def time ():
    d=t.strftime ("%d-%m-%Y , %H:%M:%S %p")
    lable_A.config (text=d)
    lable_A.after (1000, time)


lable_A=Label ( font=('Arial' ,25),  bg="black", fg="yellow")
lable_A.pack()

lable_b = Label (master=frame_b, text="I'm in Frame B")
frame_b.pack()

time()
mainloop()