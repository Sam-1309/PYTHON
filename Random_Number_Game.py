import random as r
from  tkinter import *
from tkinter import messagebox
mainwindow=Tk()
mainwindow.title("RANDOM-NUMBER GAME")
mainwindow.geometry("200x100")
label=Label(mainwindow,text="ENTER NUMBER")
label.pack()
entry=Entry(mainwindow)
entry.pack()

def random_num():
     point=0
     num=int(entry.get())
     random=r.randint(1 ,100)
     while num==random:
            messagebox.showerror("!!!!!","WIN...WIN")
            point+=5

     else :
         messagebox.showerror("!!!!!!!","TRY_AGAIN")
     return point
button=Button(mainwindow,text="RANDOM NUMBER",command=random_num)
button.pack()
mainwindow.mainloop()