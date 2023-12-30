from reportlab.lib.pagesizes import A4, landscape
from lists_and_dictionaries import *
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

# Avoid using the name 'list' for a variable
def generate_pdf():
# registrace Arial fontu
    registerFont(TTFont('Arial', 'ARIAL.ttf'))

# registrace Arial fontu
    stylesheet = getSampleStyleSheet()
    normal = stylesheet['Normal']
    custom = ParagraphStyle('custom', parent=normal)
    custom.fontName = 'Arial'
    custom.alignment = TA_CENTER
    custom.fontSize = 11
    custom.rowHeight = 12

# vytvoření layoutu
    nazev_pdf = 'příloha [B].pdf'
    pdf_layout = SimpleDocTemplate(nazev_pdf, pagesize=landscape(A4), topMargin=5)

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

# data lists
    main_table_data = [
        ["Požární úsek: " + list_nazvy_pu_default[0].cget("text"),"","","","","","","","",""],["m.č.", "Název místnosti/prostoru", Paragraph("<para>S<sub>i</sub></para>", style=custom), Paragraph("<para>h<sub>si</sub></para>", style=custom), Paragraph("<para>p<sub>si</sub> okna</para>", style=custom), Paragraph("<para>p<sub>si</sub> dveře</para>", style=custom), Paragraph("<para>p<sub>si</sub> podlaha</para>", style=custom), Paragraph("<para>p<sub>si</sub></para>", style=custom), "ČSN 73 0802, tab. A.1", Paragraph("<para>p<sub>ni</sub></para>", style=custom), Paragraph("<para>a<sub>ni</sub></para>", style=custom)],
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

    záhlaví = [["příloha [C]", "Posouzení požárního rizika dle ČSN 73 0802", ""]]

    main_table_style = TableStyle([
        ("SPAN", (0, 0), (-1, 0)),
        ("ALIGN", (0, 0), (0, 0), "LEFT"),
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.75,0.75,0.75)),
        ('BACKGROUND', (0, 1), (-1, 1), colors.Color(0.875,0.875,0.875)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 1), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 1), 5),
        ('BACKGROUND', (0, 2), (-1, -1), colors.beige),

        ('LINEBEFORE', (1, 1), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
    ])


# Add borders to main table


# create main table and set style
    main_table = Table(main_table_data)
    main_table.setStyle(main_table_style)


# Alternate background color
    for i in range(2, len(main_table_data)):
        if i % 2 == 0:
            bc = colors.beige
        else:
            bc = colors.burlywood

        main_table_border_style = TableStyle([('BACKGROUND', (0, i), (-1, i), bc)])
        main_table.setStyle(main_table_border_style)




    table_záhlaví_style = TableStyle([

        ('BACKGROUND', (0, 0), (-1, 0), colors.white),  # Header background color
        ('FONTNAME', (0, 0), (-1, 0), 'Arial'),

    ])
    table_záhlaví_style.add('ALIGN', (0, 0), (0, -1), 'LEFT')  # Left-align the first column
    table_záhlaví_style.add('ALIGN', (1, 0), (1, 0), 'CENTER')


# create heading and set style
    table_záhlaví = Table(záhlaví, colWidths=pdf_layout.pagesize[0] / 3 - 10, rowHeights=11)
    table_záhlaví.setStyle(table_záhlaví_style)

# create blank space
    space_25 = Spacer(width=0, height=25)
    elems = [table_záhlaví, space_25, main_table]

    pdf_layout.build(elems)
