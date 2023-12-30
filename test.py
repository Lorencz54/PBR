from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

fileName = 'table_with_paragraph.pdf'
pdf = SimpleDocTemplate(fileName, pagesize=A4, topMargin=5)  # Adjust topMargin as needed

registerFont(TTFont('Arial', 'ARIAL.ttf'))


# Sample data for the main_table

stylesheet = getSampleStyleSheet()
normal = stylesheet['Normal']
custom = ParagraphStyle('custom', parent=normal)
custom.fontName = 'Arial'
custom.alignment = TA_CENTER
custom.textColor = colors.whitesmoke

data = [
    ['Name', "data", Paragraph("<para>S<sub>i</sub></para>", style=custom)],
    ['John Doe', 30, 'Engineer'],
    ['Jane Smith', 25, 'Teacher'],
    ['Bob Johnson', 35, 'Doctor'],
]




# Create a main_table with the sample data
table = Table(data)

záhlaví = [["příloha [C]", "PBŘ"]]
table_2 = Table(záhlaví, colWidths=pdf.pagesize[0] / 2 - 10, rowHeights=11)
style_2 = TableStyle([

    ('BACKGROUND', (0, 0), (-1, 0), colors.white),  # Header background color
    ('FONTNAME', (0, 0), (-1, 0), 'Arial'),

])
style_2.add('ALIGN', (0, 0), (0, -1), 'LEFT')  # Left-align the first column
style_2.add('ALIGN', (-1, 0), (-1, -1), 'RIGHT')
table_2.setStyle(style_2)

# Add main_table_style to the main_table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align all cells
    ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Add grid lines

])




table.setStyle(style)


# Build the PDF document with both the spacer, paragraph, and the main_table
pdf.build([table_2, table])
