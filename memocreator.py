from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c=canvas.Canvas("simple.pdf",pagesize=letter)
c.drawString(20,100,"hello world")
c.save()