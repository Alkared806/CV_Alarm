import tkinter as tk
import time as t
import Budilnik
import threading


window = tk.Tk()
window.title("CLOCK")
window.geometry("400x100")

frame_a = tk.Frame()
frame_b = tk.Frame()

def time ():
    d=t.strftime ("%d-%m-%Y , %H:%M:%S %p")
    label_a.config (text=d)
    label_a.after (1000, time)

label_a = tk.Label(font=('Arial' ,25),  bg="black", fg="yellow" )
label_a.pack()


time()

clear_thread = threading.Thread(target= Budilnik.BLUD, daemon=True).start()

window.mainloop()