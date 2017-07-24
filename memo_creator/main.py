from memocrator import pdf

#Gerardo estas son las variables a cambiar 
Data = {"Aula": "EIA204", "expedicion" : "03/07/2017","vencimiento":" - 10/07/2017", "entrada" : "16:00 hrs","salida" : "23:00 hrs","Materia":"Electronica Aplicada"}
Students=["Pedro Calderon de La barca","Name2","Name3","Name4",""]
ID=["A01225057","A01234567","A01255757","A02340123",""]
Material=[[1,2,3,4,5,6,7,8,9],["osciloscopio","fuente","multimetro","","","","","",""]]

pdf.Set_Header(1)
pdf.Load_logo()
pdf.Load_Table(0)
pdf.Material_Table()
pdf.First_Params(Data)
pdf.Names(Students,ID,0)
pdf.Material_List(Material,0)
pdf.Before_Material()
pdf.Last_paragraph()

pdf.Next_page()
pdf.Set_Header(2)
pdf.Load_logo()
pdf.Load_Table(115)
pdf.Material_table()
pdf.Material_List(Material,70)
pdf.signatures(Students)
pdf.Names(Students,ID,115)
pdf.Date_Place(Data)
pdf.Compromiso(Students,ID)
pdf.Horario_escrito(Data)
pdf.Rules()
pdf.END_Document()

pdf.Open_File()