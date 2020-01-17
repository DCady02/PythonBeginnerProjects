import shutil
import os
import time

x = True

def sorter():

	for foldername, subfolders, filenames in os.walk("C:\\users\\danie\\downloads"):
		for file in filenames:
			name, ext = os.path.splitext(file)
			ext = ext.lower()

			if ext == '.pdf':
				shutil.move("C:\\users\\danie\\downloads\\" + file, "C:\\users\\danie\\documents\\pdf")
			elif ext == '.exe':
				shutil.move("C:\\users\\danie\\downloads\\" + file, "C:\\users\\danie\\documents\\executables")
			elif ext == '.png' or ext == '.jpg' or ext == '.jpeg':
				shutil.move("C:\\users\\danie\\downloads\\" + file, "C:\\Users\\danie\\Pictures\\downloaded")


while x is True:
	sorter()
	time.sleep(1)