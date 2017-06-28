from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . models import Quote
from io import BytesIO
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
import cStringIO as StringIO


def generate_quote_pdf(quote):

    
    context_dictionary = {
        "quote": quote
    }

    template = get_template("pdfs/quote.html")
    context = Context(context_dictionary)
    html = template.render(context_dictionary)

    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)

    new_file = open("quotes/test.pdf", "w")
    
    pisaStatus = pisa.CreatePDF(
        html.encode('utf-8'),
        dest = new_file,
        encoding = 'utf-8'
    )

    new_file.close()
    


def send_quote(quote):
     pass
