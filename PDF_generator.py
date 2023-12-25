from reportlab.pdfgen import canvas
from lists_and_dictionaries import *
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

registerFont(TTFont('Arial','ARIAL.ttf'))

def generate_pdf():
    # Create a PDF document
    pdf = canvas.Canvas(output_pdf)
    pdf.setPageSize(landscape(A4))
    # záhlaví
    pdf.setFont("Arial", 11)
    pdf.setFillColor(Color(0.5, 0.5, 0.5))
    pdf.drawString(350, 580, "Stanovení požárního rizika")
    pdf.drawString(10, 580, "PBŘ - příloha [B]")

    # nadpis tabulky místností
    pdf.setFillColor(Color(0, 0, 0))
    pdf.drawString(10, 550, "Požární úsek: {}".format(str(list_nazvy_pu_default)))
    pdf.drawString(10, 530, "m.č.")
    pdf.drawString(50, 530, "název místnosti / prostoru")
    pdf.drawString(200, 530, "Si")
    pdf.drawString(240, 530, "Hsi")
    pdf.drawString(280, 530, "psi okna")
    pdf.drawString(340, 530, "psi dveře")
    pdf.drawString(400, 530, "psi podlaha")
    pdf.drawString(470, 530, "psi")
    pdf.drawString(500, 530, "ČSN 73 0802, tab. A.1")
    pdf.drawString(620, 530, "pni")
    pdf.drawString(660, 530, "ani")
    # Add content to the PDF


    pdf.drawString(10, 480, 'Variable 1: {}'.format(dic_m_rows))
    # Add more lines as needed

    # Save the PDF
    pdf.save()

# Example variables
variable1 = 10
variable2 = 'Hello'
output_pdf = 'output.pdf'

# Generate the PDF
generate_pdf()