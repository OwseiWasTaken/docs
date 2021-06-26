#! /usr/bin/python3.9
#imports
from util import *

#main
class Program:
	def __init__(this,argv):
		this.argv = argv
		this.argk = list(argv.keys())
		this.ErrNum = 0
		this.BDP = BDP("cmd.py")
		this.PwdAliases = var({
			"/home/owsei":"~",
			"/Documents":"/docs"
		})

		

		# this.ExitCode is the program exit codecd

	@property
	def pwd(this):
		msg = pwd()
		for key in this.PwdAliases:
			msg = msg.replace(key,this.PwdAliases[key],1)
		# msg = msg.replace("/home/owsei","~",1)
		# msg = msg.replace("~/Documents","~/docs",1)
		return msg

	@property
	def prompt(this):
		
		nc = color["nc"]
		if this.ErrNum:
			ErrColor = color["br red"]
		else:
			ErrColor = color["br green"]
		
		msg = f"{this.pwd} {ErrColor}[{this.ErrNum}] >>>{nc} "
		return msg

	def help(this):
		print("help")
	
	def ls(this):
		if len(this.args) > 1:
			print("")
		args = this.args[0]

	def Main(this):
		commands = {"help":this.help
			,"cls":clear
			,"clear":clear
			,"clean":clear
			,"ls":this.ls
			# ,"cd":this.cd
			# ,"./":this.start
		}
		while True:
			# get line w/ prompt
			line = input(this.prompt)
			# replace no-space comamnds
			line = line.replace("./","./ ",1)
			# split line
			line = line.split()
			if line != ['\x1b[A']:
				# set comm and args
				comm = line[0]
				this.args = line[1:]
			try:
				# set $? to 0 and run command
				this.ErrNum = 0
				commands[comm]()
			except KeyError:
				# set $? to -1 if command does not exist
				this.ErrNum = -1

			# $? is the status or ErrNum


		return 0

#start
if __name__ == '__main__':
	name = argv.pop(0)
	argv = argv_assing(argv)

	if (debug:='--debug' in argv.keys()):
		start = tm()
		del argv["--debug"]

	exit_code = Program(argv).Main()

	if debug:
		if not exit_code:print(f'{color["green"]}code successfully exited in',end='')
		else:print(f'{color["red"]}code exited with error {exit_code} in',end='')
		print(f' {round(tm()-start,5)} seconds{color["nc"]}')
	exit(exit_code)
