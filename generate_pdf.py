from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from io import BytesIO
import subprocess, sys
import gzip


# Example 1

# c = canvas.Canvas("Sample.pdf")
# c.drawString(100, 600, "Pdf generation using Python-reportlab")
# c.save()

# opener = "open" if sys.platform == "darwin" else "xdg-open"
# subprocess.call([opener, "Sample.pdf"])


# In memory file write and read using python
# myio = BytesIO()

# # write bytes to zip file in memory
# with gzip.GzipFile(fileobj=myio, mode='wb') as g:
#     g.write(b"Does it work!")

# # read bytes from the zip file in memory
# with gzip.GzipFile(fileobj=myio, mode="rb") as g:
#     myio.seek(0)
#     result = g.read()

# print(result)


# Example 2
# importing modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
  
# initializing variables with values
fileName = 'sample.pdf'
documentTitle = 'sample'
title = 'Technology'
subTitle = 'The largest thing now!!'
textLines = [
    'Technology makes us aware of',
    'the world around us.',
]
image = 'profile.jpg'
  
# creating a pdf object
pdf = canvas.Canvas(fileName)
  
# setting the title of the document
pdf.setTitle(documentTitle)
  
# registering a external font in python
pdfmetrics.registerFont(
    TTFont('abc', 'Ubuntu-Regular.ttf')
)
  
# creating the title by setting it's font 
# and putting it on the canvas
pdf.setFont('abc', 36)
pdf.drawCentredString(300, 770, title)
  
# creating the subtitle by setting it's font, 
# colour and putting it on the canvas
pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subTitle)
  
# drawing a line
pdf.line(30, 710, 550, 710)
  
# creating a multiline text using 
# textline and for loop
text = pdf.beginText(40, 680)
text.setFont("Courier", 18)
text.setFillColor(colors.red)
for line in textLines:
    text.textLine(line)
pdf.drawText(text)
  
# drawing a image at the 
# specified (x.y) position
pdf.drawInlineImage(image, 85, 160)
  
# saving the pdf
pdf.save()

