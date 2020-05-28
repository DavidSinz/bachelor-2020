# __main__.py

import sys
import code
import locate
import watermark

def main():
	input_file = sys.argv[1]
	job_id = sys.argv[2]
	title = sys.argv[3]
	tmp_folder = ''
	
	if '/' in input_file:
		tmp_folder = input_file.rsplit('/',1)[0]+'/'
	
	l = locate.Locate(title)
	c = code.Code(tmp_folder+'pngcode.png', l.show_path(), 2)
	w = watermark.Watermark('watermarkcode', input_file, c.get_filename(), tmp_folder, 10, 10)
	#print(w.get_filename())

if __name__ == '__main__':
	main()

