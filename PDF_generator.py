from reportlab.pdfgen import canvas
from lists_and_dictionaries import *
def generate_pdf():
    # Create a PDF document
    pdf = canvas.Canvas(output_pdf)

    # Add content to the PDF
    pdf.drawString(100, 800, 'Variable 1: {}'.format(dic_m_rows))
    # Add more lines as needed

    # Save the PDF
    pdf.save()

# Example variables
variable1 = 10
variable2 = 'Hello'
output_pdf = 'output.pdf'

# Generate the PDF
generate_pdf()