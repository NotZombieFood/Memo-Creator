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
    def Set_Header(self):
        self.c.setFont("Helvetica-Bold", 13)
        self.c.drawString(260,725," M E M O R Á N D U M")
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
        self.c.drawString(350,575,"De: Ing. Adrián Navarro Díaz")
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
        
        
Data = {"Aula": "EIA204", "expedicion" : "03/07/2017","vencimiento":" - 10/07/2017", "entrada" : "16:00 hrs","salida" : "23:00 hrs" }

pdf=Lean_Canvas()
pdf.Set_Header()
pdf.Load_logo()
pdf.First_Params(Data)
pdf.END_Document()
pdf.Open_File()

#c=canvas.Canvas("simple.pdf",pagesize=letter)
#esponse['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

#elements = []

#doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)

#data=[(1,2),(3,4)]
#table = Table(data, colWidths=270, rowHeights=79)
#elements.append(table)
#c.build(elements) 



import os
val=os.path.dirname(os.path.realpath(__file__))+"\simple.pdf"
os.startfile(val) 

