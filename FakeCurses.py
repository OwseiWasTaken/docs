#! /usr/bin/python3.9
#imports
from util import *


#main
class program:
	def	get(this,indicators,other=[]):
		for indicator in indicators:
			if indicator in this.argk:
				for thing in this.argv[indicator]:
					other.append(thing)

	def __init__(this,argv,argk):
		# declare vars
		this.argv = argv
		this.argk = argk

		# REMEMBER [
			# CANT USE ARROW KEYS
		# ]

	def exit(this):
		exit(0)
	@staticmethod
	def print1():
		print("mode1")
	@staticmethod
	def print2():
		print("mode2")
	@staticmethod
	def print3():
		print("mode3")
	@staticmethod
	def print4():
		print("mode4")
	@staticmethod
	def print5():
		print("mode5")
	@staticmethod
	def print6():
		print("mode6")
	@staticmethod
	def print7():
		print("mode7")
	

	def MainMenu(this):
		funcs = [this.print1,this.print2,this.print3,this.print4,this.print5,this.print6,this.print7,this.exit]
		modes = ["mode1","mode2","mode3","mode4","mode5","mode6","mode7","exit"]
		y = 0
		while True:
			ch = GetCh()
			clear()

			if ch == 'w' and y:
				y-=1
			elif ch == 's' and y<len(modes)-1:
				y+=1
			elif ch == '\r':
				clear()
				funcs[y]()
				GetCh()
				clear()


			for mode in r(modes):
				msg = modes[mode]
				if y == mode:
					msg = f'{color["bk green"]}{msg}{color["bk nc"]}'
				print(msg)

	def Main(this):
		this.MainMenu()


		return 0






#start
if __name__ == '__main__':
	argv = ArgvAssing(argv[1:])
	argk = list(argv.keys())
	code = program(argv,argk).Main

	if '--debug' in argk:
		start = tm()
		ExitCode = code()

		if not ExitCode:print(f'{color["green"]}code successfully exited in',end='')
		else:print(f'{color["red"]}code exited with error {ExitCode} in',end='')
		print(f' {round(tm()-start,5)} seconds{color["nc"]}')
	else:
		ExitCode = code()
	exit(ExitCode)
