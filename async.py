#! /usr/bin/python3.9
#imports
from util import *
import asyncio
#main
def main(argv):



	return 0

#start
if __name__ == '__main__':
	start = tm()
	name = argv.pop(0)
	if (debug:='--debug' in argv):
			argv.remove('--debug')

	exit_code = main(argv)

	if debug:
		if not exit_code:
			printf(f'{color("green")}code successfully exited in {round(tm()-start,5)} second')
		else:
			print(f'{color("red")}code exited with error {exit_code} in {round(tm()-start,5)} seconds')
	printf(color('nc'))
	exit(exit_code)