#!/usr/bin/python3

import os

print('\nRemember to write #!/usr/bin/python3 at the beginning of the .py files\n')

py_files = [ x_file for x_file in os.listdir(os.curdir) if x_file.endswith('.py') ]
py_files.sort()

if len(py_files) == 1:
	elegidos = [py_files[0]]
else:
	pos = 0
	for x_file in py_files:
		print(f'[{pos:2d}] {x_file}')
		pos += 1
	print(f'[{pos:2d}] install all')

	which = int(input('\nChoose the script you want to install: '))
	if which == pos: #install all
		elegidos = py_files
	else:
		elegidos = [py_files[which]] #list so I can use a for loop

errors = []
for programa in elegidos:
	print('Installing', programa)
	a = os.system(f'sudo cp {programa} /usr/local/bin/{programa.replace(".py", "")}')
	b = os.system(f'sudo chmod a+rx /usr/local/bin/{programa.replace(".py", "")}')
	if a != 0 or b != 0:
		errors.append(programa)

if errors:
	print(f'Something went wrong with these programs:\n  {(" ").join(errors)}')