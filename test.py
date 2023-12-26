# List of Lists

# Using list comprehension to create three new lists
list1 = [dic_psi_entries[0][i] for i in range(0, len(dic_psi_entries[0]), 3)]
list2 = [dic_psi_entries[0][i] for i in range(1, len(dic_psi_entries[0]), 3)]
list3 = [dic_psi_entries[0][i] for i in range(2, len(dic_psi_entries[0]), 3)]



data = [
    ["m.č.", "název místnosti / prostoru", "Si", "Hsi", "psi okna", "psi okna", "psi dveře", "psi podlaha", "psi", "ČSN 73 0802, tab. A.1", "pni", "ani"],
    [dic_mc_text_entries[0]],
    [dic_nazvy_m_text_entries[0]],
    [dic_S_entries[0]],
    [dic_hsi_entries[0]],
    [list1],
    [list2],
    [list3],
    [dic_ps_row_sum_labels[0]],
    [dic_CSNi_entries[0]],
    [dic_pni_entries[0]],
    [dic_ani_entries[0]],
]

fileName = 'pdfTable.pdf'

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont

registerFont(TTFont('Arial','ARIAL.ttf'))

pdf = SimpleDocTemplate(fileName, pagesize=landscape(A4))

from reportlab.platypus import Table

table = Table(data)

# add style
from reportlab.platypus import TableStyle
from reportlab.lib import colors

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

# 2) Alternate backgroud color
rowNumb = len(data)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige

    ts = TableStyle(
        [('BACKGROUND', (0, i), (-1, i), bc)]
    )
    table.setStyle(ts)

# 3) Add borders
ts = TableStyle(
    [
        ('BOX', (0, 0), (-1, -1), 1, colors.black),

        ('LINEBEFORE', (2, 1), (2, -1), 1, colors.black),
        ('LINEABOVE', (0, 2), (-1, 2), 1, colors.black),

        ('GRID', (0, 1), (-1, -1), 1, colors.black),
    ]
)
table.setStyle(ts)

elems = []
elems.append(table)

pdf.build(elems)

