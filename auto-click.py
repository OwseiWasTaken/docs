#! /usr/bin/python3.8
#imports
from util import sleep,tm,exit,argv,ss
from pynput.mouse import Button,Controller
import threading
#main
def main(argv):
	if argv[-1] != argv[0]:
		st = float(argv[-1])
		sleep(ms=100)
	else:
		st = tm()
	print(st)
	ss(f"python3.8 /home/owsei/Documents/py/auto-clicker.py {tm()-st} {st} &")
	while True:
		if tm()-st > float(argv[0]):break
		Controller().click(Button.left)

	return 0

#start
if __name__ == '__main__':
	start = tm()
	name = argv.pop(0)
	exit_code = main(argv[0:])
	exit(exit_code)
