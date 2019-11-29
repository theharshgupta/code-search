
import os 
import time
import re

def get_extension(file_name: str):
	return file_name.split('.')[-1]

def search(root, indent=0):
		# print(indent*"-", f"Inside the folder: {root}")
		if len(os.listdir(root)) == 0:
			return "End of indexing reached!"
		for file in os.listdir(root):
			try: 
				if os.path.isdir(root+file):
					search(root+file+'/', indent+2)
				file_extension = get_extension(root+file)
				if file_extension == 'py' and 'venv' not in root and 'site-package' not in root and 'Anaconda' not in root:
					print((indent+2)*"-", root+file)
					with open(root+file, encoding='utf-8') as open_file:
						file_contents_str = str(open_file.read())
						print(file_contents_str)
						re_test(file_contents_str)
						# file_contents_lines = open_file.readlines()
						# for line_index, file_line in enumerate(file_contents_lines):
							# if '\"\"\"' in file_line:
								# print((indent+4)*"-", file_contents_lines[line_index+1])
					# print((indent+2)*"-", f"The extension of the above file is: {file_extension}")
			except PermissionError as permission_denied:
				print(f"Not allowed to open the following file {root+file}\n{permission_denied}")
				continue
def re_test(text: str):
	try:
		result_re = re.search(r'\"\"\"(.*?)\"\"\"', text)
		if result_re:
			print(result_re.group(1))
		else:
			print("not found")
	except Exception as e:
		print("not found", e)
# search('X:/Python/urap-scrape/')
