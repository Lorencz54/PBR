from reportlab.lib.pagesizes import A4, landscape
from lists_and_dictionaries import *
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

list_test = [1,2,3,4,5]
nazev_pdf = 'příloha [Test].pdf'
pdf_layout = SimpleDocTemplate(nazev_pdf, pagesize=landscape(A4), topMargin=5)

def generate_pdf():
    elems = []
    for j in range (len(list_test)):
        data = [
            [list_test[j]]
        ]
        tab = Table(data)
        elems.append(tab)
    pdf_layout.build(elems)

generate_pdf()

