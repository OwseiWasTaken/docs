#! /usr/bin/python3.9
#imports
from util import *

# OUTDATED USE MKF.PY INSTEAD

#main
def main(argv):
	argk = list(argv.keys())

	types = ls("/home/owsei/Templates")

	for tp in r(types):
		types[tp] = types[tp].split('.')[0]

	for arg in r(argk):
		try:
			argk[arg] = argk[arg][1:]
		except TypeError:pass

	TypesToCopy = {i:[] for i in types}



	for i in argk:
		for ii in types:
			if i in ii or i in ii[0]:
				TypesToCopy[ii] = argv[f'-{i}']


	for TypeToCopyKey in TypesToCopy.keys():
		for tt in ls("/home/owsei/Templates"):
			if tt.split('.')[0] == TypeToCopyKey:
				if TypesToCopy[TypeToCopyKey]:
					for cp in TypesToCopy[TypeToCopyKey]:
						ss(f"cp /home/owsei/Templates/{tt}* {cp}")
						# sorry for this f****** mess



	return 0

#start
if __name__ == '__main__':
	start = tm()
	name = argv.pop(0)
	if (debug:='--debug' in argv):
			argv.remove('--debug')
	try:
		argv = argv_assing(argv)
	except IndexError:
		print(f"no argument found in argv")
		exit(1)

	exit_code = main(argv)

	if debug:
		if not exit_code:
			print(f'{color["green"]}code successfully exited in',end='')
		else:
			print(f'{color["red"]}code exited with error {exit_code} in',end='')
		print(f' {round(tm()-start,5)} seconds{color["nc"]}')
	exit(exit_code)
