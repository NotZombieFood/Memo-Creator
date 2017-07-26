from Tkinter import *
import tkMessageBox
import Tkinter

#root=Tk()
#theLabel=Label(root,text="This is to easy")


top = Tk()

c=Checkbutton(top,text="Selecioname")
c.grid(row=3)

mb=  Menubutton ( top, text="condiments", relief=RAISED )

mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 ) 
mb["menu"]  =  mb.menu    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )
entry_1=Entry(top)
entry_1.grid(row=1)

def callback(event):
    print "hellow world"
    print mayoVar.get()
    print entry_1.get()

mb.bind("<Button-1>",callback)

mb.grid(row=0)
top.mainloop()


