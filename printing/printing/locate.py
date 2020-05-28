import os
import os.path
import subprocess

class Locate:

	def __init__(self, title):
		self.title = title

	def show_path(self):
		result_paths = []
		for dirpath, dirnames, filenames in os.walk('/home'):
			for f in filenames:
				file_ext = ''
				file_path = os.path.join(dirpath, f)
				
				if len(f.rsplit('.',1)) > 1:
					file_ext = f.rsplit('.',1)[1]
					
				if f == self.title:
					result_paths.append(file_path)
				elif file_ext == 'pdf':
					result = subprocess.run(['pdfinfo', file_path], stdout=subprocess.PIPE)
					if self.title in str(result.stdout):
						result_paths.append(file_path)
		if len(result_paths) > 0:
			return result_paths[0]
		else:
			return 'no filepath'

