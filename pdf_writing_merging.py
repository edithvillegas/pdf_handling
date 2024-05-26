# imports (install reportlab) -----------
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfReader, PdfWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

import os

# file paths -----------------------------
input_file='pdf_files/input_file.pdf'
output_file='pdf_files/output_file.pdf'
watermark_file='pdf_files/watermark_file.pdf'

# create PDF ----------------------------

#canvas
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFont(psfontname='Courier', size=5, leading = None)

#write origin
can.drawString(0, 0, "Origin")

#write coordinates
for i_height in range(0, 600, 10):
    for i_width in range(0, 150, 10)
        can.drawString(i_width, i_height, f"{i_width},{i_height}")

can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfReader(packet)

# merge with input PDF --------------------
# read your existing PDF
existing_pdf = PdfReader(open(f"{input_file}", "rb"))
output = PdfWriter()

# add the new pdf on the existing page
existing_page = existing_pdf.pages[0]
existing_page.merge_page(new_pdf.pages[0])

# merge with another file
existing_pdf = PdfReader(open(f"{watermark_file}", "rb"))
watermark_page = existing_pdf.pages[0]
existing_page.merge_page(watermark_page)

# finally, write "output" to a real file
output_stream = open(f"{output_file}", "wb")

output.add_page(existing_page)
output.write(output_stream)
output_stream.close()