'''
Make sure That You Have A file named remainder in the folder in which 
You are putting this digital calendar
'''

from tkinter import *
import calendar
import datetime
import plyer 
from plyer import notification
def notifyMe(message):
    notification.notify(
        title = message[:10],
        message = message[10:],
        timeout = 30
    )
root = Tk()
root.title("Calendar")
year = datetime.datetime.today().year
month = datetime.datetime.today().month
today0 = calendar.month(year,month)
today1 = datetime.datetime.today().date
out = Text(root, height=10, width=20, bg="black", fg="white")
out.pack()
remainder_btn = Button(root, text="Set Remainder")
out.insert(1.0, today0, today1)
f = open("remainder.txt", "r")
remainder = str(f.read())

    
if str(datetime.datetime.today().date()) in remainder:
    notifyMe(remainder)
else:
    out.insert(END, "--------------------")
    out.insert(END, "Today is " + str(datetime.datetime.today().date()))
inp = input()
inp1 = input()
with open("remainder.txt", "w") as f:
    f.write(str(inp)+"\n"+str(inp1))
f.close()
root.mainloop()
