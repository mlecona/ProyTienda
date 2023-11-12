""" Ejemplo de Conversion a PDF con pyppeteer"""

from django.shortcuts import render 

import asyncio
from pyppeteer import launch

async def generate_pdf(url, pdf_path):
    """ Generar PDF desde la URL de un sitio web """
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    await browser.close()

# Run the function
asyncio.get_event_loop().run_until_complete(generate_pdf('https://example.com', 'example.pdf'))

async def generate_pdf_from_html(html_content, pdf_path):
    """ Genere PDF a partir de contenido HTML personalizado """
    browser = await launch()
    page = await browser.newPage()
    
    await page.setContent(html_content)
    
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    
    await browser.close()

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

# Run the function
asyncio.get_event_loop().run_until_complete(generate_pdf_from_html(html_content, 'from_html.pdf'))
