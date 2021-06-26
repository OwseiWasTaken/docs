#! /usr/bin/python3.9
#imports
from util import *

#main
class program:
	def __init__(this,argv,argk):
		# declare vars
		this.argv = argv
		this.argk = argk
		this.bdp = BDP("dirs.py")
		try:
			this.root = this.bdp.load()
		except FileNotFoundError:
			this.root = {"/":{}}


	def AddDir(this,name,Path):
		# path = list
		# name = str
		Path = Path.split('/')
		for PathIndex in r(Path):
			Path[PathIndex] = f'{Path[PathIndex]}/'
		Path.pop(-1)
		if name[-1] != '/':
			name+='/'
		contents = '{}'
		dir = ''.join([f"[\"{di}\"]" for di in Path])
		
		exec(f"this.root{dir}[\"{name}\"] = {contents}")

	def AddFile(this,name,content,Path):
		# path = list
		# name = str
		# dir = ''.join([f"[\"{di}\"]" for di in path])
		Path = Path.split('/')
		for PathIndex in r(Path):
			Path[PathIndex] = f'{Path[PathIndex]}/'

		Path.pop(-1)

		Path =  ''.join([f"[\"{dir}\"]" for dir in Path])
		name = repr(name)

		exec(f"this.root{Path}[{name}] = \"{content}\"")



	def Main(this):
		while True:
			IPT = input()
			if "mkdir " in IPT:
				this.AddDir(IPT[6:],'/')

			elif "touch " in IPT:
				this.AddFile(IPT[6:],"wowowo",'/')
			
			elif "ls" in IPT:
				print(this.root)

		print(this.root)



		this.bdp.save(this.root)
		return 0






#start
if __name__ == '__main__':
	argv = argv_assing(argv[1:])
	argk = list(argv.keys())
	code = program(argv,argk).Main

	if '--debug' in argk:
		start = tm()
		ExitCode = code()

		if not ExitCode:print(f'{color["green"]}code successfully exited in',end='')
		else:print(f'{color["red"]}code exited with error {exit_code} in',end='')
		print(f' {round(tm()-start,5)} seconds{color["nc"]}')
	else:
		ExitCode = code()
	exit(ExitCode)
