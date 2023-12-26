from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from lists_and_dictionaries import *

# Avoid using the name 'list' for a variable
def generate_pdf():
    psi_okna = []
    psi_dvere = []
    psi_podlahy = []
    for i in range(len(dic_psi_entries[0])):
        if i % 3 == 0:
            psi_podlahy.append(dic_psi_entries[0][i])
        elif i % 3 == 1:
            psi_dvere.append(dic_psi_entries[0][i])
        else:
            psi_okna.append(dic_psi_entries[0][i])
    data = [
        ["m.č.", "Název místnosti/prostoru", "Si", "hsi", "psi okna", "psi dveře", "psi podlaha", "psi", "ČSN 73 0802, tab. A.1", "pni", "ani"],
        *[
            [mc_entry.get(), nazvy_m_entry.get(), S_entry.get(), hsi_entry.get(), psi_okna_entry.get(), psi_dvere_entry.get(), psi_podlahy_entry.get(), psi_sum_entry, CSN_entry.get(), pni_entry.get(), ani_entry.get(), ]
            for mc_entry, nazvy_m_entry, S_entry, hsi_entry, psi_okna_entry, psi_dvere_entry, psi_podlahy_entry, psi_sum_entry, CSN_entry, pni_entry, ani_entry in zip(
                dic_mc_text_entries[0],
                dic_nazvy_m_text_entries[0],
                dic_S_entries[0],
                dic_hsi_entries[0],
                psi_okna,
                psi_dvere,
                psi_podlahy,
                dic_ps_group_sums[0],
                dic_CSNi_entries[0],
                dic_pni_entries[0],
                dic_ani_entries[0]
            )
        ],
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
