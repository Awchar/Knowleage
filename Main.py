import Knowleage
from tkinter import *


root = Tk()
root.geometry('480x480')
root.title('Knowleage V0.0.1')

button1 = Button(root,text='Show All Database',command=Knowleage.Show_All_Data)
button1.place(x=100,y=100)



root.mainloop()