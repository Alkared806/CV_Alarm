import datetime
import threading
from playsound import playsound
from Capture import video

def music_task():
    playsound ("1.mp3") 

date_entry = input("Enter datetime (Год-Месяц-День-Часы-Минуты) -->")
year, month, day, hour, minute  = map(int,date_entry.split("-"))
deadline = datetime.datetime(year, month, day, hour, minute)

print('Deadline time: {}.'.format(deadline.strftime('%d/%m/%Y %H:%M')))

while True:
    now = datetime.datetime.now()
    print('Current time: {}.    '.format(now.strftime('%d/%m/%Y %H:%M:%S')), end='\r')

    if now >= deadline:
        print(end='\n' "WAKE UP!")
        break

clear_thread = threading.Thread(target=music_task, daemon=True).start()   
video()
