from tkinter import *
from time import *

j=Tk()
local = localtime()
j.geometry('300x150')

l=Label(j,text=f'Hora local: {strftime("%H:%M:%S", local)}')
l.place(x=30,y=20)
ed=Button(j,width=10,text='resetar')
ed.place(x=30,y=75)
j.mainloop()