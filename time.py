from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import pytz 
import time

root=Tk()

root.title("this time will also pass")
root.geometry("1500x900")

India=Label(root,text="India",font=("times",20,"bold"))
India.place(relx=0.2,rely=0.2,anchor=CENTER)

USA=Label(root,text="USA",font=("times",20,"bold"))
USA.place(relx=0.8,rely=0.2,anchor=CENTER)

img=ImageTk.PhotoImage(Image.open("clock.jpg"))

Ind=Label(root)
Ind["image"]=img
Ind.place(relx=0.2,rely=0.4,anchor=CENTER)

USA=Label(root)
USA["image"]=img
USA.place(relx=0.8,rely=0.4,anchor=CENTER)

Iblank=Label(root)
Iblank.place(relx=0.2,rely=0.8,anchor=CENTER)

Ublank=Label(root)
Ublank.place(relx=0.8,rely=0.8,anchor=CENTER)

class India ():
    def times(self):
        home=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        Iblank["text"]="time: "+current_time
        Iblank.after(200,self.times)
        
class USA ():
    def times(self):
        home=pytz.timezone("US/Central")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        Ublank["text"]="time: "+current_time
        Ublank.after(200,self.times)

obj_India=India()
obj_USA=USA()


Ibtn=Button(root,text="show time",command=obj_India.times)
Ibtn.place(relx=0.2,rely=0.6,anchor=CENTER)

Ubtn=Button(root,text="show time",command=obj_USA.times)
Ubtn.place(relx=0.8,rely=0.6,anchor=CENTER)




root.mainloop()