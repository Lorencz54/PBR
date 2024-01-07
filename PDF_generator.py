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

# paragraphs design
    stylesheet = getSampleStyleSheet()
    normal = stylesheet['Normal']
    custom = ParagraphStyle('custom', parent=normal)
    custom.fontName = 'Arial'
    custom.alignment = TA_CENTER
    custom.fontSize = 11
    custom.rowHeight = 12


    stylesheet = getSampleStyleSheet()
    normal = stylesheet['Normal']
    custom_2 = ParagraphStyle('custom_2', parent=normal, textColor=colors.red)
    custom_2.fontName = 'Helvetica-Bold'
    custom_2.alignment = TA_CENTER
    custom_2.fontSize = 13
    custom_2.rowHeight = 14

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

    záhlaví_data = [
        ["příloha [B]", "Posouzení požárního rizika dle ČSN 73 0802", ""]
    ]

    second_table_data = [
        ["S", str(list_S[0]), Paragraph("<para>m<sup>2</sup></para>", style=custom),"","","","",Paragraph("<para>a<sub>n</sub></para>", style=custom), str(list_an[0]), "","","","","","součinitel a", str(list_a[0]), ""],
    [Paragraph("<para>h<sub>s</sub></para>", style=custom), str(list_hs[0]), "m","","","","",Paragraph("<para>p<sub>n</sub></para>", style=custom), str(list_pn[0]), "","","","","","součinitel b", str(list_b[0]), ""],
    [Paragraph("<para>p<sub>s</sub></para>", style=custom), str(list_ps[0]), Paragraph("<para>kg/m<sup>2</sup></para>", style=custom),"","","","",Paragraph("<para>S<sub>o</sub></para>", style=custom), str(list_so[0]), Paragraph("<para>m<sup>2</sup></para>", style=custom),"","","","","součinitel c", "1.0", ""],
    [Paragraph("<para>S<sub>o</sub>/S</para>", style=custom), str(list_pomer_S_So[0]), "", "", "", "", "", "n", str(list_n[0]), "", "", "", "", "", "zatížení p", str(list_pn[0]), Paragraph("<para>kg/m<sup>2</sup></para>", style=custom)],
    [Paragraph("<para>h<sub>o</sub>/S</para>", style=custom), str(list_ho[0]),"m","","","","", Paragraph("<para>S<sub>m</sub></para>", style=custom), str(list_Sm[0]), Paragraph("<para>m<sup>2</sup></para>", style=custom),"","","","",Paragraph("<para>p<sub>v</sub></para>", style=custom_2), list_pv[0], Paragraph("<para>kg/m<sup>2</sup></para>", style=custom_2)],
    [Paragraph("<para>h<sub>o</sub>/h<sub>s</sub></para>", style=custom), str(list_pomer_ho_hs[0]), "", "", "", "", "", "k", str(list_k[0]), "", "", "", "", "", "", "", ""],
    ]

    pv_result_data = [
        [Paragraph("<para>p<sub>v</sub></para>", style=custom), list_pv[0], Paragraph("<para>kg/m<sup>2</sup></para>", style=custom)]
    ]

    third_table_data = [
        ["konstrukční systém", list_konstrukcni_systemy[0],"", "", "počet podlaží PÚ", list_pocty_podlazi_PU[0], "", "", "max. počet podlaží", list_max_pocty_podlazi_PU[0], ""],
        ["požární výška objektu", list_e_pozarni_vyska[0].get(), "m", "", "skutečná šířka PÚ", list_e_sirky_pu[0].get(), "m", "", "mezní šířka PÚ", list_mezni_sirky[0].get(), "m"],
        ["výšková poloha PÚ", list_vyskove_polohy_pu[0].get(),"", "", "skutečná délka PÚ", list_e_delky_pu[0].get(), "m", "", "mezní délka PÚ", list_mezni_delky[0].get(), "m"],
    ]
    result_string = "požární úsek "+list_nazvy_pu_default[0].cget("text")+" je zařazen do "+str(list_SPB[0])+"stupně požární bezpečnosti"
    fourth_table_data = [
        [result_string]
    ]
    main_table_style = TableStyle([
        ("SPAN", (0, 0), (-1, 0)),
        ("ALIGN", (0, 0), (0, 0), "LEFT"),
        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0.75,0.75,0.75)),
        ('BACKGROUND', (0, 1), (-1, 1), colors.Color(0.875,0.875,0.875)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 1), 5),
        ('BACKGROUND', (0, 2), (-1, -1), colors.beige),
        ('LINEBEFORE', (1, 1), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
    ])

    second_table_style = TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.Color(0.875, 0.875, 0.875)),
        ('BACKGROUND', (7, 0), (7, -1), colors.Color(0.875, 0.875, 0.875)),
        ('BACKGROUND', (14, 0), (14, -1), colors.Color(0.875, 0.875, 0.875)),
        ('BACKGROUND', (14, 4), (16, 5), colors.white),
        ("SPAN", (3, 0), (6, -1)),
        ("SPAN", (10, 0), (13, -1)),
        ("SPAN", (14, 4), (14, 5)),
        ("SPAN", (15, 4), (15, 5)),
        ("SPAN", (16, 4), (16, 5)),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('LINEBEFORE', (1, 0), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
        ('TEXTCOLOR', (15, 4), (15, 4), colors.red),
        ('FONTSIZE', (15, 4), (15, 4), 13),
        ('FONTNAME', (15, 4), (15, 4), 'Helvetica-Bold'),

    ])

    third_table_style = TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.Color(0.875, 0.875, 0.875)),
        ('BACKGROUND', (4, 0), (4, -1), colors.Color(0.875, 0.875, 0.875)),
        ('BACKGROUND', (8, 0), (8, -1), colors.Color(0.875, 0.875, 0.875)),
        ("SPAN", (3, 0), (3, -1)),
        ("SPAN", (7, 0), (7, -1)),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('LINEBEFORE', (1, 0), (-1, -1), 1, colors.black),
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, -1), (-1, -1), 1, colors.black),
    ])

    fourth_table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.875, 0.875, 0.875)),
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.red),
    ])


    pv_result_table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.Color(0.875, 0.875, 0.875)),
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBELOW', (0, 0), (-1, -1), 1, colors.black),
        ('LINEBEFORE', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
        ('ALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (2, 0), (2, 0), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.red),
    ])
# create main table and set style
    main_table = Table(main_table_data)
    main_table.setStyle(main_table_style)

# Alternate background color for main table
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
    table_záhlaví = Table(záhlaví_data, colWidths=pdf_layout.pagesize[0] / 3 - 10, rowHeights=11)
    table_záhlaví.setStyle(table_záhlaví_style)

# create second table and set style
    second_table = Table(second_table_data, rowHeights=23, colWidths=(70, 70, 50, 5, 5, 5, 5, 70, 70, 50, 5, 5, 5, 5, 70, 70, 50))

    #pv_result_table = Table(pv_result_data, rowHeights=23, colWidths=(pdf_layout.pagesize[0]-91.8897637795277) / 3)
    #pv_result_table.setStyle(pv_result_table_style)

    third_table = Table(third_table_data, rowHeights=23, colWidths=(110, 70, 50, 20, 110, 70, 50, 20, 110, 70, 50))
    third_table.setStyle(third_table_style)

    fourth_table = Table(fourth_table_data, colWidths=pdf_layout.pagesize[0]-91.8897637795277)
    fourth_table.setStyle(fourth_table_style)
# Alternate background color for second table
    for i in range(len(second_table_data)):
        if i % 2 == 0:
            bc = colors.beige
        else:
            bc = colors.burlywood

        second_table_style_2 = TableStyle([
            ('BACKGROUND', (1, i), (2, i), bc),
            ('BACKGROUND', (8, i), (9, i), bc),
            ('BACKGROUND', (15, i), (16, i), bc),
        ])

        second_table.setStyle(second_table_style_2)
    second_table.setStyle(second_table_style)

    for i in range(len(third_table_data)):
        if i % 2 == 0:
            bc = colors.beige
        else:
            bc = colors.burlywood

        third_table_style = TableStyle([
            ('BACKGROUND', (1, i), (2, i), bc),
            ('BACKGROUND', (5, i), (6, i), bc),
            ('BACKGROUND', (9, i), (10, i), bc),
        ])

        third_table.setStyle(third_table_style)


# create blank space
    space_25 = Spacer(width=0, height=25)
    elems = [table_záhlaví, space_25, main_table, space_25, second_table, space_25, third_table, space_25, fourth_table]

    pdf_layout.build(elems)
