import os
import pyqrcode

class Code:

	def __init__(self, filename, string, scale):
		self.filename = filename
		self.string = string
		self.scale = scale
		self.create()

	def create(self):
		code = pyqrcode.create(self.string)
		code.png(self.filename, scale=self.scale, background=[0xff, 0xff, 0xff])
		#print(self.filename)

	def get_filename(self):
		return self.filename

	def __del__(self):
        	os.remove(self.filename)

