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
    def Load_Table(self,offset):
        self.c.drawImage("tablauno.jpg",80,420+offset,width=6*inch, height=1*inch)
    def Names(self,*args):
        self.c.setFont("Times-Bold",12)
        name=args[0]
        ID=args[1]
        i=0
        y=465+args[2]
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
        self.c.setFont("Times-Bold",12)
        Material=args[0]
        Cantidad=Material[0]
        Tipo=Material[1]
        i=0
        y=355+args[1]
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
        self.c.drawString(350,670,"Guadalajara, Jalisco a "+self.number_to_month(Date))
        
    def Compromiso(self,*args):
        Name=args[0]
        ID=args[1]
        self.c.drawString(53,640,"Yo")
        self.c.setFont("Times-BoldItalic", 12)
        x=72
        self.c.drawString(x,640,Name[0])
        x+=(len(Name[0])*5.5)
        self.c.setFont("Times-Roman",12)
        self.c.drawString(x,640," estudiante de ITE con matricula")
        x+=159
        self.c.setFont("Times-BoldItalic", 12)
        self.c.drawString(x,640,ID[0])
        x+=57
        self.c.setFont("Times-Roman",12)
        self.c.drawString(x,640," hago constar que estaré")
        self.c.drawString(53,625,"estaré trabajando en Laboratorio de electrónica junto con mi equipo, conformado por:")
    def Horario_escrito(self,*args):
        Entrada=args[0]["entrada"]
        Salida=args[0]["salida"]
        Horario=args[0]["entrada"]+" a "+args[0]["salida"]
        Expedicion=self.number_to_month(args[0]["expedicion"])+" a "
        Vencimiento=self.number_to_month(args[0]["vencimiento"][3:])
        self.c.drawString(53,515,"El horario en el que estaremos trabajando es de "+Horario+" del día "+Expedicion)
        self.c.drawString(53,500,Vencimiento+" La razón por la que necesitamos trabajar en este horario es porque es la hora en la que")
        self.c.drawString(53,485,"terminamos clases realizaremos un proyecto de la materia "+args[0]["Materia"])
        self.c.drawString(53,470,"Para ello necesitamos el siguiente material: ")
    def number_to_month(self,date):
        dia=str(int(date[0:2]))
        months=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        mes=months[int(date[3:5])-1]
        final=dia+" de "+ mes+" del "+date[6:10]
        return final
    def Material_table (self):
        self.c.drawImage("tablados.jpg",80,370,width=6*inch, height=1.1*inch)
    def Rules(self):
        self.c.drawString(53,350,"Me comprometo a cumplir con el reglamento del laboratorio y hacer que mis compañeros de equipo ")
        self.c.drawString(53,335,"también lo cumplan. De esta manera nos hacemos responsables por el daño que sufran el equipo y las")
        self.c.drawString(53,320,"instalaciones tras nuestra estadía en el laboratorio. Aceptando trabajar bajo las siguientes condiciones:")
        self.c.drawString(103,290,"1. Cumplir con el reglamento general para laboratorios.")
        self.c.drawString(103,275,"2. Cuidar el inmueble durante su estancia en el laboratorio.")
        self.c.drawString(103,260,"3. Reportar al laboratorista cualquier comportamiento inapropiado o circunstancia extraña ")
        self.c.drawString(103,245,"que suceda y note durante el tiempo que esté trabajando en el laboratorio.")
        self.c.drawString(103,230,"4. No se podrá trabajar en el laboratorio si hay clases programadas. Por lo que no se")
        self.c.drawString(103,215,"aceptarán memorándums con horarios que se empalmen con las clases.")
        self.c.drawString(103,200,"5. Una vez terminado su trabajo se deberá recoger su lugar de trabajo y dejar el equipo")
        self.c.drawString(103,185,"prestado en la mesa de materiales.")
        self.c.drawString(103,170,"6. El alumno deberá avisar a algún guardia que pase cerrar el laboratorio en caso de terminar")
        self.c.drawString(103,155,"antes de la hora indicada.")
        self.c.drawString(103,140,"7. Cualquier circunstancia fuera del reglamento estará a consideración de la coordinación de")
        self.c.drawString(103,125,"laboratorios para definir la sanción correspondiente.")
    def signatures(self,*args):
        self.c.line(100,80,250,80)
        self.c.line(300,80,480,80)
        self.c.drawString(100,60,args[0][0])
        self.c.drawString(330,60,"Ing. Alejandro Gallegos")
        
pdf=Lean_Canvas()





