from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from lists_and_dictionaries import *

# Avoid using the name 'list' for a variable
def generate_pdf():
    my_list = []
    for i in range(len(dic_mc_text_entries[0])):
        my_list.append(dic_mc_text_entries[0][i].get())

    data = [
        ["m.č."],
        my_list,
    ]

    fileName = 'pdfTable.pdf'

    registerFont(TTFont('Arial', 'ARIAL.ttf'))

    pdf = SimpleDocTemplate(fileName, pagesize=landscape(A4))
    table = Table(data)

    # Add style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    table.setStyle(style)

    # Alternate background color
    for i in range(1, len(data)):
        if i % 2 == 0:
            bc = colors.burlywood
        else:
            bc = colors.beige

        ts = TableStyle([('BACKGROUND', (0, i), (-1, i), bc)])
        table.setStyle(ts)

    # Add borders
    ts = TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBEFORE', (2, 1), (2, -1), 1, colors.black),
        ('LINEABOVE', (0, 2), (-1, 2), 1, colors.black),
        ('GRID', (0, 1), (-1, -1), 1, colors.black),
    ])

    table.setStyle(ts)

    elems = [table]

    pdf.build(elems)
