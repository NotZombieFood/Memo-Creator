# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class Lean_Canvas():
    def __init__(self):
        self.c=canvas.Canvas("simple.pdf",pagesize=letter)
    def Load_logo(self):
        self.c.drawImage("Captura.jpg",100,720,width=1.7*inch, height=.6*inch)
    def Set_Header(self,page):
        self.c.setFont("Helvetica-Bold", 13)
        if(page is 1):
            self.c.drawString(260,725," M E M O R Á N D U M")
        else:
            self.c.drawString(260,725," Carta de Responsabilidad")
        self.c.setLineWidth(.7)
        self.c.line(80,700,540,700)
        self.c.line(80,697,540,698)        
    def First_Params(self,*args):
        #titulos
        params=args[0]
        self.c.setFont("Times-BoldItalic", 12)
        self.c.drawString(54,680,"Asunto:")
        self.c.drawString(53,665,"Fecha de expedición:")
        self.c.drawString(53,635,"Fecha de solicitud del laboratorio:")
        self.c.drawString(53,620,"Hora de entrada:")
        self.c.drawString(53,605,"Hora de salida:")
        self.c.drawString(350,575,"De: Ing. Alejandro Gallegos")
        self.c.drawString(335,560,"Departamento de ITE")
        #datos
        self.c.setFont("Times-Roman",12)
        self.c.drawString(97,680,"Uso del Laboratorio de")
        self.c.drawString(210,680,params["Aula"])
        self.c.drawString(162,665,params["expedicion"])
        self.c.drawString(227,635,params["expedicion"]+params["vencimiento"])
        self.c.drawString(140,620,params["entrada"])
        self.c.drawString(133,605,params["salida"])
        #parrafo
        self.c.drawString(53,545,"De la manera más atenta, es mi responsabilidad notificarles que los alumnos enlistados laborarán en el")
        self.c.drawString(264,530,"en la fecha mencionada, por lo que les pido les permitan la")
        self.c.drawString(193,530,", aula ")
        self.c.drawString(53,515,"estancia durante el horario marcado, así como evitar que algún alumno ajeno a esta relación pueda")
        self.c.drawString(53,500,"acceder a esta área. Los alumnos que podrán trabajar son:")
        
        self.c.setFont("Times-Bold",12)
        self.c.drawString(53,530,"Laboratorio de electronica")
        self.c.drawString(222,530,params["Aula"])
    def END_Document(self):
        self.c.save()
    def Open_File(self):
        import os
        val=os.path.dirname(os.path.realpath(__file__))+"\simple.pdf"
        os.startfile(val) 
    def Load_Table(self):
        self.c.drawImage("tablauno.jpg",80,420,width=6*inch, height=1*inch)
    def Names(self,*args):
        name=args[0]
        ID=args[1]
        i=0
        y=465
        while(name[i] is not ""):
            self.c.drawString(82,y,name[i])
            self.c.drawString(412,y,ID[i])
            y-=14
            i+=1
    def Before_Material(self):
        self.c.setFont("Times-Roman",12)
        self.c.drawString(53,400,"A continuación se les asigna el siguiente equipo del cual, los alumnos nombrados se harán responsables")
    def Material_Table(self):
        self.c.drawImage("material.jpg",80,230,width=6*inch, height=2.1*inch)
                         
    def Material_List(self,*args):
        Material=args[0]
        Cantidad=Material[0]
        Tipo=Material[1]
        i=0
        y=355
        while(Tipo[i] is not ""):
            self.c.drawString(108,y,str(Cantidad[i]))
            self.c.drawString(150,y,Tipo[i])
            y-=14
            i+=1
    def Last_paragraph(self):
        self.c.drawString(53,200,"De igual manera les solicitamos por favor que estén al pendiente de alguna irregularidad que se")
        self.c.drawString(53,185,"presente durante el transcurso de estas labores y que las notifiquen a la brevedad posible a las")
        self.c.drawString(53,170,"autoridades correspondientes. De antemano, gracias.")
        self.c.drawString(53,140,"Saludos")
        self.c.setLineWidth(.7)
        self.c.line(180,100,400,100)
        self.c.drawString(220,80,"Ing. Alejandro Gallegos")
    def Next_page(self):
        self.c.showPage()
    #######page 2
    def Date_Place(self,*args):
        self.c.setFont("Times-Roman",12)
        Date=args[0]["expedicion"]
        dia=str(int(Date[0:2]))
        months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        mes=months[int(Date[3:5])-1]        
        self.c.drawString(350,670,"Guadalajara, Jalisco a "+dia+" de "+ mes+" del "+Date[6:10])
       
Data = {"Aula": "EIA204", "expedicion" : "03/07/2017","vencimiento":" - 10/07/2017", "entrada" : "16:00 hrs","salida" : "23:00 hrs" }
Students=["Name1","Name2","Name3","Name4",""]
ID=["A01225057","A01234567","A01255757","A02340123",""]
Material=[[1,2,3,4,5,6,7,8,9],["osciloscopio","fuente","multimetro","","","","","",""]]

pdf=Lean_Canvas()
pdf.Set_Header(1)
pdf.Load_logo()
pdf.Load_Table()
pdf.Material_Table()
pdf.First_Params(Data)
pdf.Names(Students,ID)
pdf.Material_List(Material)
pdf.Before_Material()
pdf.Last_paragraph()

pdf.Next_page()
pdf.Set_Header(2)
pdf.Load_logo()
pdf.Date_Place(Data)
pdf.END_Document()

pdf.Open_File()




