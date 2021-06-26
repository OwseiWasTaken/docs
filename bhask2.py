#! /usr/bin/python3.9
#imports
from util import *

#main
def main(argv):
	if [True for i in ['-a','-b','-c'] if i in argv.keys()] == [True,True,True]:
		a,b,c,var_symb = float(argv["-a"][0]),float(argv["-b"][0]),float(argv["-c"][0]),'x'

	elif "-f" in argv.keys():
		frm = argv['-f']
		for form in frm:
			var_symb = form.find("²")
			num_to_square = float(form[var_symb-2])
			var_symb = form[var_symb-1]
			if num_to_square in ['+','-']:
				num_to_square = 1

			a = num_to_square*num_to_square

			form = form.split('+')
			for i in form:
				if '²' in i:
					form.pop(
					form.index(i)
					)
					break
			for i in form:
				print(i,var_symb,var_symb in i)
				if var_symb in i:
					b = eval(i[:-1])
				else:
					c = eval(i)


	delta = ((b**2) - (4*a*c))**.5
	x = (-b + delta)/(a*2)
	y = (-b - delta)/(a*2)
	print(f'''
{var_symb} pos:{x}
{var_symb} neg:{y}
	''')

	return 0

#start
if __name__ == '__main__':
	start = tm()
	name = argv.pop(0)
	if (debug:='--debug' in argv):
			argv.remove('--debug')
	exit_code = main(argv_assing(argv))

	if debug:
		if not exit_code:
			print(f'code successfully exited in',end='')
		else:
			print(f'code exited with error {exit_code} in',end='')
		print(f' {round(tm()-start,5)} seconds')
	exit(exit_code)
