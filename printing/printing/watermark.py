import os
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader

class Watermark:

	def __init__(self, name, input_filename, code_filename, tmp_folder, margin_left, margin_bottom):
		self.name = name
		self.input_filename = input_filename
		self.output_filename = tmp_folder+'document-output.pdf'.format(name)
		self.watermark = tmp_folder+'watermark-{0}.pdf'.format(name)
		self.code = code_filename
		self.x = margin_left
		self.y = margin_bottom
		self.create_watermark()
		self.insert_watermark()

	def create_watermark(self):
		c = canvas.Canvas(self.watermark)
		c.drawImage(self.code, self.x, self.y)
		c.save()
	
	def insert_watermark(self):
		watermark_pdf = PdfFileReader(open(self.watermark, 'rb'))
		document = PdfFileReader(open(self.input_filename, 'rb'))
		output_file = PdfFileWriter()
		for i in range(document.getNumPages()):
			page = document.getPage(i)
			page.mergePage(watermark_pdf.getPage(0))
			output_file.addPage(page)
		with open(self.output_filename, 'wb') as outputStream:
			output_file.write(outputStream)
		
	def get_filename(self):
		return self.output_filename
	
	def __del__(self):
        	os.remove(self.watermark)

