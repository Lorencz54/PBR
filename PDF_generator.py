from reportlab.pdfgen import canvas
from lists_and_dictionaries import *
from reportlab.lib.colors import Color

def generate_pdf():
    # Create a PDF document
    pdf = canvas.Canvas(output_pdf)

    # Set font characteristics (italic and grey color)
    pdf.setFont("Helvetica-Oblique", 12)  # You can use a different font and size
    pdf.setFillColor(Color(0.5, 0.5, 0.5))  # Grey color

    # Draw the text with the specified font and color
    pdf.drawString(230, 820, "Stanovení požárního rizika")


    # Reset font and color to default (optional)
    pdf.setFont("Helvetica", 12)  # Set it to your default font and size
    pdf.setFillColor(Color(0, 0, 0))

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