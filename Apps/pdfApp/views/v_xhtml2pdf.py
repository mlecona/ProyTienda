""" Ejemplo de Conversion a PDF con from xhtml2pdf import pisa
"""

from django.shortcuts import render

from xhtml2pdf import pisa
import requests

def convert_url_to_pdf(url, pdf_path):
    """ Para generar PDF desde la URL de un sitio web """
    # Fetch the HTML content from the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch URL: {url}")
        return False
    
    html_content = response.text
    
    # Generate PDF
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)
        
    return not pisa_status.err

# URL to fetch
url_to_fetch = "https://google.com"

# PDF path to save
pdf_path = "google.pdf"

# Generate PDF
if convert_url_to_pdf(url_to_fetch, pdf_path):
    print(f"PDF generated and saved at {pdf_path}")
else:
    print("PDF generation failed")
    
""" Generar PDF a partir de contenido HTML personalizado """
def convert_html_to_pdf(html_string, pdf_path):
    """ Generar PDF a partir de contenido HTML personalizado """
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)
        
    return not pisa_status.err

# HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>PDF Example</title>
</head>
<body>
    <h1>Hello, world!</h1>
</body>
</html>
"""

# Generate PDF
pdf_path = "example.pdf"
if convert_html_to_pdf(html_content, pdf_path):
    print(f"PDF generated and saved at {pdf_path}")
else:
    print("PDF generation failed")