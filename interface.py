from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

Titulo=Label(top,text="Memo Creator").grid(row=0,column=2)
Salon=Label(top,text="Salon").grid(row=1,column=0)
Compas=Label(top,text="Compañeros").grid(row=1,column=2)
Label_dia=Label(top,text="Dia").grid(row=2,column=4)
Label_year=Label(top,text="Año").grid(row=2,column=5)

start=  Menubutton ( top, text="Set", relief=RAISED )
start.grid(row=1,column=3)
start.menu  =  Menu ( start, tearoff = 0 ) 

renta= Menubutton ( top, text="Duración", relief=RAISED )
renta.grid(row=4,column=4)
renta.menu  =  Menu ( renta, tearoff = 0 ) 
renta["menu"]=renta.menu
days= IntVar()
renta.menu.add_radiobutton( label="1",variable=days,value=1)
renta.menu.add_radiobutton( label="2",variable=days,value=2)
renta.menu.add_radiobutton(label="3",variable=days,value=3)
renta.menu.add_radiobutton(label="4",variable=days,value=4)
renta.menu.add_radiobutton(label="5",variable=days,value=5)
renta.menu.add_radiobutton(label="6",variable=days,value=6)
renta.menu.add_radiobutton(label="semana",variable=days,value=7)



mb=  Menubutton ( top, text="Mes", relief=RAISED )
mb.grid(row=3,column=3)
mb.menu  =  Menu ( mb, tearoff = 0 ) 
mb["menu"]  =  mb.menu    
Mes  = IntVar()


mb.menu.add_radiobutton( label="Enero",
                          variable=Mes,value=1)
mb.menu.add_radiobutton( label="Febrero",
                          variable=Mes,value=2)
mb.menu.add_radiobutton( label="Marzo",
                         variable=Mes,value=3)
mb.menu.add_radiobutton( label="Abril",
                         variable=Mes,value=4)
mb.menu.add_radiobutton( label="Mayo",
                         variable=Mes,value=5)
mb.menu.add_radiobutton( label="Junio",
                         variable=Mes,value=6)
mb.menu.add_radiobutton( label="Julio",
                         variable=Mes,value=7)
mb.menu.add_radiobutton( label="Agosto",
                         variable=Mes,value=8)
mb.menu.add_radiobutton( label="Septiembre",
                         variable=Mes,value=9)
mb.menu.add_radiobutton( label="Octubre",
                         variable=Mes,value=10)
mb.menu.add_radiobutton( label="Noviembre",
                         variable=Mes,value=11)
mb.menu.add_radiobutton( label="Diciembre",
                         variable=Mes,value=12)




dia=Entry(top,width=3)
dia.grid(row=3,column=4)
year=Entry(top,width=6)
year.grid(row=3,column=5)

def callback(event):
     print "hellow world"
     if(Salones.get() is 0 or NumeroC.get() is 0):
          Warning=Label(top,text="Select an option!!!").grid(row=1,column=4)
     else:
          print Salones.get()
          print NumeroC.get() 
          lines=[Entry(top,width=3)]*NumeroC.get()
          i=0
          for n in lines:
               print i
               lines[i].grid(row=5+i,column=6)
               i+=1
               

start.bind("<Button-1>",callback)

Salones = IntVar()

Radiobutton(top, text="204", variable=Salones, value=204).grid(row=2)
Radiobutton(top, text="207", variable=Salones, value=207).grid(row=3)
Radiobutton(top, text="208", variable=Salones, value=208).grid(row=4)
Radiobutton(top, text="210", variable=Salones, value=210).grid(row=5)

NumeroC=IntVar()

Radiobutton(top, text="1", variable=NumeroC, value=1).grid(row=2,column=2)
Radiobutton(top, text="2", variable=NumeroC, value=2).grid(row=3,column=2)
Radiobutton(top, text="3", variable=NumeroC, value=3).grid(row=4,column=2)
Radiobutton(top, text="4", variable=NumeroC, value=4).grid(row=5,column=2)

top.mainloop()


