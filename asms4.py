#! /usr/bin/python3.9

from util import *
clear()

# todo
# make funcs
# make more asm comms

plan = """
[
make everything in a class (so i can use this.var instead of "global var")
comments HAVE to be //
# no multi line comments (yet) sorry
]

1°
make list of file (file, but cleaned)
del \n
sep coms by ;
and remove comments

2°
sep commands and args
use () for args and , to different stuff
# formating
COMMAND(arg1,arg2,arg3)
# like
MOV(3,%varname)
PRT($varname)
# out:
# 3

3°
exec stuff
"""




class program:
	@property
	def VARK(this):
		return list(this.VARS.keys())

	def ShowFileOut(this):
		ss(f"{this.cat} {this.FileOut}")

	def __init__(this):
		this.fnow = None
		this.VARS = {
			"FLG" : False
			,"ACC" : 0
			,"EXT" : 0
		}

		this.argv = argv_assing(argv)
		this.argk = list(this.argv.keys())

		# debugging
		this.debug_mode = False
		if '--debug' in this.argk:
			this.debug_mode = eval(this.argv["--debug"][0])


		# lolcat or car
		this.lolcat = False
		if '-lcat' in this.argk:
			this.lolcat = eval(this.argv['-lcat'][0])
		if this.lolcat:
			this.cat = "lolcat"
		else:
			this.cat = "cat"


		# ReadExecutinFile
		this.rf = False
		if '-rf' in this.argk:
			this.rf = eval(this.argv['-rf'][0])
		if this.rf:
			print("##################")

		# def FileIn name
		this.FileIn = this.argv['-i'][0]
		with open(this.FileIn,'r') as Infile:
			this.FileIn=";".join(Infile.read().split('\n')).split(';')

		# def StdIn
		this.StdIn = []
		if '-s' in this.argk:
			this.StdIn = this.argv['-s'][0]
			with open(this.StdIn,'r') as StdInfile:
				this.StdIn=StdInfile.read().split('\n')

		# def FileOut
		this.FileOut = "out.txt"
		if '-o' in this.argk:
			this.FileOut = argv["-o"][0]


		this.Log = log(tm=False)
		this.Log.LOG = []
		this.Log.add(f"in    : {this.FileIn}")
		this.Log.add(f"stdout: {this.FileOut}")
		this.Log.add(f"StdIn : {this.StdIn}")
		this.Log.add('')

		this.commands = {"END":this.END
		,"NOP":this.NOP
		,"PRT":this.PRT
		,"MOV":this.MOV
		,"RNG":this.RNG
		,"INW":this.INW
		,"TST":this.TST
		,"ADD":this.ADD
		,"SUB":this.SUB
		,"MUL":this.MUL
		,"DIV":this.DIV
		,"EXT":this.EXT
		,"SLP":this.SLP
		,"ORD":this.ORD
		,"CHR":this.CHR
		,"DEL":this.DEL
		,"OSC":this.OSC
		,"EXS":this.EXS
		,"DEF":this.DEF
		,"SPT":this.SPT
		,"SPL":this.SPL
		,"LEN":this.LEN
		,"JMP":this.JMP
		}

		# clean this.FileIn
		this.MakeList()
		
		this.line=0
		while inrange(this.line,this.FileIn):
			this.ExecLine(this.FileIn[this.line])
			this.line+=1

		
		print('##################\n')
		if this.debug_mode:
			[print(f"{k} : {this.VARS[k]}") for k in this.VARS.keys()]

	def ExecLine(this,line):
		line = var(line)
		line = line.SplitBracket('(')
		ln = []
		for word in line:
			if word:
				ln.append(word)
		line = ln
		command = line.pop(0)

		try:
			args = line[0].split(',')
		except IndexError:
			args = line

		if not command in ["DEF","INW","END"]:
			BetterArgs = []
			for arg in args:
				BetterArgs.append(this.get(arg))
			args = BetterArgs
		if command == "END":
			this.fnow = None

		if this.rf:
			print(f"{command}:{args}")
		if this.fnow == None:
			command = this.commands[command]
			if type(command) == list:
				for FuncLine in command:
					this.ExecLine(FuncLine)
			else:
				command(args)
		else:
			this.commands[this.fnow].append(f"{command}({str(args)[1:-1]})")




	def MakeList(this):
		# MOV(1,%a);MOV(4,%b)
		result = []
		removes = ['\t','\n']
		if this.FileIn[0][0:2] == '#!':
			this.FileIn = this.FileIn[1:]

		for ln in r(this.FileIn):
			# remove \n and \t (removes list)
			for rem in removes:
				this.FileIn[ln] = this.FileIn[ln].replace(rem,'')

			# if all the line is a comment remove the line
			if this.FileIn[ln][0:2] == '//':continue

			# remove comments
			if (keep:=this.FileIn[ln].find('//')) != -1:
				this.FileIn[ln] = this.FileIn[ln][:keep]
	
			# add line if line != ''
			if this.FileIn[ln]:
				result.append(this.FileIn[ln])

		this.FileIn = result

	def get(this,value:str):
		# return VARS[value] or eval(value)
		print(value)
		if value[0:2] == 'f"':
			value = split_bracket(value[2:-1],'{')

			for ValueIndex in r(value,start=1,jmp=2):
				value[ValueIndex] = str(this.get(value[ValueIndex]))
			ret = ''.join(value)
			ret = ret.replace('\\t','\t')
			ret = ret.replace('\\n','\n')
		else:
			try:
				if value in this.VARK:
					ret = this.VARS[value]
				else:
					ret = eval(value)
			except SyntaxError:
				ret = value
		
		
		return ret



# asms funcs
	def END(this,args):pass

	def NOP(this,args):pass

	def MOV(this,args):

		if len(args) == 2:
			from_,to_ = args
		
		if len(args) == 1:
			from_,to_ = "None",args[0]
		

		this.VARS[to_] = from_

	def RNG(this,args):
		rnumber = rint(
		min(float(args[0]),float(args[1])),
		max(float(args[0]),float(args[1]))
		)
		if len(args) == 2:
			this.MOV((rnumber,"RNG"))
		elif len(args) == 3:
			this.MOV((rnumber,args[-1]))

	def JMP(this,args):
		this.line = args[0]


	def INW(this,args):
		if args == []:
			this.VARS["INR"] = this.StdIn.pop(0)
		else:
			this.VARS[args[0]] = this.StdIn.pop(0)

	def DEF(this,args):
		this.fnow = args.pop(0)
		this.commands[this.fnow] = []

	def PRT(this,args):
		msg = ""
		for arg in args:
			msg+=f"{arg}"

		sout.write(msg)
	
	def TEQ(this,args):
		if type(args[-1]) == str:
			st = args.pop(0)[1:]
		else:
			st="FLG"

		this.VARS[st] = True
		for ar1 in r(args):
			for ar2 in r(args):
				if args[ar1] != args[ar2]:
					this.VARS[st] = False

	def TGT(this,args):
		if type(args[-1]) == str:
			st = args.pop(-1)[1:]
		else:
			st="FLG"
	
		if len(args) == 2:
			this.VARS[st] = args[0] > args[1]
		elif len(args) == 1:
			this.VARS[st] = args[0] > this.VARS["ACC"]

	def TST(this,args):
		if type(args[-1]) == str:
			st = args.pop(0)[1:]
		else:
			st="FLG"
		
		if len(args) == 2:
			this.VARS[st] = args[0] < args[1]
		elif len(args) == 1:
			this.VARS[st] = args[0] < this.VARS["ACC"]

	def EXS(this,args):
		if type(args[-1]) == str:
			st = args.pop(0)[1:]
		else:
			st="FLG"
		this.VARS[st] = args[0] in this.VARK()
	

	def ADD(this,args):
		if len(args) == 2:
			add_ = args[0]
			to_  = args[1][1:]

		if len(args) == 1:
			add_ = args[0]
			to_  = "ACC"
		try:
			this.VARS[to_]+=add_
		except TypeError:
			this.VARS[to_].append(add_)

	def SUB(this,args):
		if len(args) == 2:
			add_ = args[0]
			to_  = args[1][1:]

		if len(args) == 1:
			add_ = args[0]
			to_  = "ACC"
		try:
			this.VARS[to_]-=add_
		except TypeError:
			this.VARS[to_].remove(add_)

	def MUL(this,args):
		if len(args) == 2:
			add_ = args[0]
			to_  = args[1][1:]

		if len(args) == 1:
			add_ = args[0]
			to_  = "ACC"

		this.VARS[to_]*=add_

	def DIV(this,args):
		if len(args) == 2:
			add_ = args[0]
			to_  = args[1][1:]

		if len(args) == 1:
			add_ = args[0]
			to_  = "ACC"

		this.VARS[to_]/=add_

	def EXT(this,args):
		exit(int(args[0]))
	
	def SLP(this,args):
		for i in args:
			slp(int(i))
	
	def ORD(this,args):
		this.MOV(ord(args[0]),args[1])

	def CHR(this,args):
		this.MOV(chr(args[0]),args[1])
	
	def DEL(this,args):
		for i in args:
			del this.VARS[i]
	
	def OSC(this,args):
		for com in args:
			if com[0:2] == 'cd':
				cd(com[2:])
			else:
				ss(com)

	def SPT(this,args):
		print(f"from {args[0]} take {args[1]} (index) and make {args[2]}")
		this.MOV((args[0][args[1]],args[2]))

	def SPL(args):
		pass

	def LEN(this,args):
		# |list|var|
		print(repr(args[0]),repr(args[1]))
		this.MOV((len(args[0]),args[1]))





program()