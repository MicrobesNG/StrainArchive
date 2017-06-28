from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . models import Quote
from io import BytesIO
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
import cStringIO as StringIO

# uses django template to create a pdf file for quote
def generate_quote_pdf(quote):

    # put quote into context dictionary for template
    context_dictionary = {
        "quote": quote
    }

    # get the template
    template = get_template("pdfs/quote.html")
    # generate the html
    html = template.render(context_dictionary)

    # open new file for writing pdf to
    new_file = open("quotes/test.pdf", "w")
    
    # generate pdf and write to new file
    pisaStatus = pisa.CreatePDF(
        html.encode('utf-8'),
        dest = new_file,
        encoding = 'utf-8'
    )

    # close file once data written
    new_file.close()
    


def send_quote(quote):
     pass
