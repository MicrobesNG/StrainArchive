from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from . models import Quote
from io import BytesIO
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa


def generate_quote_pdf(quote, template_path):

    
    pass

def send_quote(quote):
     pass
