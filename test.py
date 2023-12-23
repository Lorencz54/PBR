from reportlab.pdfgen import canvas

def generate_pdf(variable1, variable2, output_pdf):
    # Create a PDF document
    pdf = canvas.Canvas(output_pdf)

    # Add content to the PDF
    pdf.drawString(100, 800, 'Variable 1: {}'.format(variable1))
    pdf.drawString(100, 780, 'Variable 2: {}'.format(variable2))
    # Add more lines as needed

    # Save the PDF
    pdf.save()

# Example variables
variable1 = 10
variable2 = 'Hello'
output_pdf = 'outpu1t.pdf'

# Generate the PDF
generate_pdf(variable1, variable2, output_pdf)
