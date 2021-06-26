#! /usr/bin/python3.9
#imports
from util import *

#main
class Program:
	def __init__(this,argv):
		this.argv = argv
		this.argk = list(argv.keys())


		this.ExitCode = this.Main()

	def Main(this):



		return 0

#start
if __name__ == '__main__':
	name = argv.pop(0)
	argv = argv_assing(argv)

	if (debug:='--debug' in argv.keys()):
		start = tm()
		del argv["--debug"]

	exit_code = Program(argv).ExitCode

	if debug:
		if not exit_code:print(f'{color["green"]}code successfully exited in',end='')
		else:print(f'{color["red"]}code exited with error {exit_code} in',end='')
		print(f' {round(tm()-start,5)} seconds{color["nc"]}')
	exit(exit_code)
