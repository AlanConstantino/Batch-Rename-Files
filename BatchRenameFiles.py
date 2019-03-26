import os
import sys

# functions
def renameFiles(path, newName):
	count = 0
	for filename in os.listdir(path):
		oldExtension = os.path.splitext(filename)
		src = path + "\\" + filename
		dest = path + "\\" + newName + str(count) + oldExtension[1]
		os.rename(src, dest)
		count += 1

def renameFilesAndExtension(path, newName, newExtension):
	count = 0
	for filename in os.listdir(path):
		src = path + "\\" + filename
		dest = path + "\\" + newName + str(count) + "." + newExtension
		os.rename(src, dest)
		count += 1

def renameFileExtension(path, newExtension):
	for filename in os.listdir(path):
		oldName = os.path.splitext(filename)
		src = path + "\\" + filename
		dest = path + "\\" + oldName[0] + "." + newExtension
		os.rename(src, dest)

# start
numberOfArgs = len(sys.argv) - 1

if numberOfArgs == 1:
	print('Error: You need to specify least two command-line arguments.')
	sys.exit()

if numberOfArgs == 2:
	path = sys.argv[1]
	newName = sys.argv[2]
	renameFiles(path, newName)
	sys.exit()

if numberOfArgs == 3:
	path = sys.argv[1]
	newName = sys.argv[2]
	newExtension = sys.argv[3]
	if newName.strip() == "0":
		renameFileExtension(path, newExtension)
	else:
		renameFilesAndExtension(path, newName, newExtension)
	sys.exit()