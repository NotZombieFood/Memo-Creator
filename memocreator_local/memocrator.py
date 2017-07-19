# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont

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
        self.c.line(80,698,540,698)        
    def First_Params(self):
        self.c.setFont("Times-BoldItalic", 12)
        self.c.drawString(50,680,"Asunto:")
        self.c.setFont("Times-Roman",12)
        self.c.drawString(92,680,"Uso del Laboratorio de")        
        
    def END_Document(self):
        self.c.save()
    def Open_File(self):
        import os
        os.startfile("C:\Users\Emilio Tonix\Documents\memocreator_local\simple.pdf")        

pdf=Lean_Canvas()
pdf.Set_Header()
pdf.First_Params()
pdf.END_Document()
pdf.Open_File()



