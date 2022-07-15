#!/usr/bin/python3

import os

class Py_file:
	def __init__(self, f_name):
		self.name = f_name

	def install(self):
		a = os.system(f'sudo cp {self.name} /usr/local/bin/{self.name.replace(".py", "")}')
		b = os.system(f'sudo chmod a+rx /usr/local/bin/{self.name.replace(".py", "")}')
		if a != 0 or b != 0:
			print(f'Something went wrong with {self.name}')

class Py_folder:
	def __init__(self, f_name):
		self.name = f_name

	def install(self):
		folder_name = self.name + '_rx'
		a = os.system(f'sudo cp -r {self.name} /usr/local/bin')
		os.chdir('/usr/local/bin')
		b = os.system(f'sudo mv {self.name} {folder_name}')
		c = os.system(f'sudo chmod a+rx /usr/local/bin/{folder_name}/{self.name}.py')
		d = os.system(f'sudo ln -s /usr/local/bin/{folder_name}/{self.name}.py {self.name}')
		if a != 0 or b != 0 or c != 0 or d != 0:
			print(f'Something went wrong with {self.name}')

def install(list_files_folders):
	for file_or_folder in list_files_folders:
		if file_or_folder.find('.') != -1: #file
			print(f'Installing {file_or_folder}')
			py_file = Py_file(file_or_folder)
			py_file.install()
		else:
			folder = Py_folder(file_or_folder)
			folder.install()

print('\nRemember to write #!/usr/bin/python3 at the beginning of the .py files\n')

files_and_folders = [ x_file for x_file in os.listdir(os.curdir) ]

files_and_folders.sort()

if len(files_and_folders) == 1:
	install(files_and_folders)

else:
	pos = 0
	for file_or_folder in files_and_folders:
		print(f'[{pos:2d}] {file_or_folder}')
		pos += 1
	print(f'[{pos:2d}] install all')

	which = int(input('\nChoose the script you want to install: '))

	if which == pos: #install all
		install(files_and_folders)

	else:
		install([files_and_folders[which]]) #list so I can use a for loop
