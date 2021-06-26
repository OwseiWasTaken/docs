#! /bin/python3.8
from util import *
clear()

# todo
# DEF(args) (maybe pdf sdf)

VARS = {
	 "STT" : 0
	,"FLG" : False
	,"ACC" : 0
	,"EXT" : 0
	,"rbool" : bool(rint(0,1))
}
VARK = lambda : list(VARS.keys())

argv = argv_assing(argv)
argk = argv.keys()

rf = False
debug_mode = False
if None in argk:
	debug_mode = True

lolcat = False
if '-lcat' in argk:
	lolcat = eval(argv['-lcat'][0])
if lolcat:
	def ShowFileOut():
		ss(f"lolcat {fileout}")
else:
	def ShowFileOut():
		ss(f"cat {fileout}")
if '-rf' in argk:
	rf = eval(argv['-rf'][0])
if rf:
	print("##################")

filein = argv['-i'][0]

stdin = []
if '-s' in argk:
	stdin = argv['-s'][0]
	with open(stdin,'r') as stdinfile:
		stdin=stdinfile.read().split('\n')

fileout = "out.txt"
if '-o' in argk:
	fileout = argv["-o"][0]

re = True
if '-re' in argk:
	re = eval(argv['-re'][0])


Log = log(tm=False)
Log.LOG = []
Log.add(f"in    : {filein}")
Log.add(f"stdout: {fileout}")
Log.add(f"stdin : {stdin}")
Log.add('')


class exec_line:
	def __init__(self,string):
		# string=string.split(",")
		# string=" ".join(string)
		string=string.split(" ")
		string_splited=-1
		try:
			while True:
				string_splited+=1
				if string[string_splited][-1]== '\\':
					string[string_splited] = " ".join([string[string_splited][:-1],string.pop(string_splited+1)])
					string_splited-=2
					continue
		except IndexError:pass
		com = string.pop(0)

		self.ln = [com,string]



def clean_line(line):
	# print(f"b:{repr(line)}")

	# line = line[:interception]
	removes = ['\t','\n']
	for rem in removes:
		line = line.replace(rem,'')
	if (keep:=line.find('//')) != -1:
		line = line[:keep]
	if (keep:=line.find('#!')) != -1:
		line = line[:keep]
	for char in r(line):
		if line[char] == '\/':
			line[char] = '/'

	# print(f"a:{repr(line)}")
	if line:return exec_line(line).ln
	else:return 0


# asms defs

def END(args):pass

def NOP(args):pass

def MOV(args):
	if len(args) == 2:
		from_,to_ = args
	elif len(args) == 1:
		from_,to_ = None,args[0]
	if to_[0] != '%':
		print(f"\
{color['red']}\
==========\
WARNING var addres doesn't start with %\
==========\
{color['nc']}\
")
		to_="%"+to_
	VARS[to_[1:]] = from_

def RNG(args):
	rnumber = rint(
		min(float(args[0]),float(args[1])),
		max(float(args[0]),float(args[1])))
	if len(args) == 2:
		MOV((rnumber,"%RNG"))
	elif len(args) == 3:
		MOV((rnumber,args[-1]))

def INW(args):
	if re:
		if args == [None]:
			VARS["INR"] = eval(stdin.pop(0))
		else:
			VARS[args[0][1:]] = eval(stdin.pop(0))
	else:
		if args == [None]:
			VARS["INR"] = stdin.pop(0)
		else:
			VARS[args[0][1:]] = stdin.pop(0)

def TEQ(args):
	if type(args[-1]) == str:
		if args[-1][0] == '%':
			st = args.pop(0)[1:]
		else:
			st = "FLG"
	else:
		st="FLG"

	VARS[st] = True
	for ar1 in r(args):
		for ar2 in r(args):
			if args[ar1] != args[ar2]:
				VARS[st] = False

def TGT(args):
	if type(args[-1]) == str:
		if args[-1][0] == '%':
			st = args.pop(-1)[1:]
		else:
			st = "FLG"
	else:
		st="FLG"
	if len(args) == 2:
		VARS[st] = args[0] > args[1]
	elif len(args) == 1:
		VARS[st] = args[0] > VARS["ACC"]

def TST(args):
	if type(args[-1]) == str:
		if args[-1][0] == '%':
			st = args.pop(0)[1:]
		else:
			st = "FLG"
	else:
		st="FLG"
	if len(args) == 2:
		VARS[st] = args[0] < args[1]
	elif len(args) == 1:
		VARS[st] = args[0] < VARS["ACC"]

def EXS(args):
	if type(args[-1]) == str and if args[-1][0] == '%':
		st = args.pop(0)[1:]
	else:
		st="FLG"
	VARS[st] = args[0] in VARK()

def PRT(args):
	try:
		args = " ".join(args)
	except Exception:pass

	if fruning == None:
		args=split_bracket(args,'{')
		for i in range(1,len(args),2):
			if args[i] in VARK():
				args[i] = VARS[args[i]]
			else:
				args[i] = eval(args[i])
	else:
	
		args=split_bracket(args,'{')
		
		for i in range(1,len(args),2):
			if args[i] in VARK():
				args[i] = VARS[args[i]]
			else:
				args[i] = eval(args[i])
		try:
			args = ''.join(args)
		except TypeError:
			if type(args) == dict:
				r = []
				for i in args.keys():
					r.append((args[i],i))
				args = r
		args = split_bracket(args,'{')

		for i in range(1,len(args),2):
			if args[i] in VARK():
				args[i] = VARS[args[i]]
			else:
				try:
					args[i] = eval(args[i])
				except SyntaxError:
					pass
	
	out.write(f"{''.join([f'{a}' for a in args])}")

def ADD(args):
	if len(args) == 2:
		add_ = args[0]
		to_  = args[1][1:]

	if len(args) == 1:
		add_ = args[0]
		to_  = "ACC"
	try:
		VARS[to_]+=add_
	except TypeError:
		VARS[to_].append(add_)

def SUB(args):
	if len(args) == 2:
		sub_ = args[0]
		to_  = args[1][1:]
		VARS[to_]-=sub_

	if len(args) == 1:
		sub_ = args[0]
		to_  = "ACC"
		VARS[to_]-=sub_

def MUL(args):
	if len(args) == 2:
		mul_ = args[0]
		to_  = args[1][1:]
		VARS[to_]*=mul_

	if len(args) == 1:
		mul_ = args[0]
		to_  = "ACC"
		VARS[to_]*=mul_


def DIV(args):
	if len(args) == 2:
		div_ = args[0]
		to_  = args[1][1:]
		VARS[to_]/=div_

	if len(args) == 1:
		div_ = args[0]
		to_  = "ACC"
		VARS[to_]/=div_

def EXT(args):
	VARS["EXT"] = args[0]

def SLP(args):
	for i in args:
		sleep(seg=i)

def ORD(args):
	MOV(ord(args[0]),args[1])

def CHR(args):
	MOV(chr(args[0]),args[1])

def DEL(args):
	for arg in args:
		if arg[0] != '%':
			arg = f'%{arg}'
		del VARS[arg[1:]]

def OSC(args):
	com = " ".join(args)
	if com[0:2] == 'cd':
		cd(com[2:])
	else:
		ss(com)

FVARS,function,fnow,fruning = {},{},None,None
def DEF(args):
	global FVARS,function,fnow,commands
	fname = args.pop(0)
	commands[fname] = fname
	function[fname]=[]
	fnow = fname
	FVARS[fname]={arg.split('=')[0]:eval(arg.split('=')[1]) if arg.find('=') != -1 else None for arg in args}

def SPT(args):
	print(f"from {args[1]} take {args[0]} (index) and make {args[2]}")
	MOV((args[1][args[0]],args[2]))

def SPL(args):
	pass

def LEN(args):
	# |list|var|
	print(repr(args[0]),repr(args[1]))
	MOV((len(args[0]),args[1]))


commands_list = ["END"
,"NOP"
,"MOV"
,"RNG"
,"INW"
,"TEQ"
,"TGT"
,"TST"
,"PRT"
,"ADD"
,"SUB"
,"MUL"
,"DIV"
,"EXT"
,"SLP"
,"ORD"
,"CHR"
,"DEL"
,"OSC"
,"EXS"
,"DEF"
,"SPT"
,"SPL"
,"LEN"
]




commands = {f : eval(f) for f in commands_list}

def RUN(command,argvs):
	global fnow,fruning
	if command[0] == '+':
		if VARS["FLG"]:
			command = command[1:]
		else:
			return
	if command[0] == '-':
		if not VARS["FLG"]:
			command = command[1:]
		else:
			return
	if rf:
		if not fnow:
			print(f"com: {repr(command)} || arg: {repr(argvs)}")
		else:
			print(f"fnc: {repr(fnow)} || com: {repr(command)} || arg: {repr(argvs)}")

	if command == "END":fnow,fruning = None,None

	if fnow == None:
		if type(commands[command]) == str:
			fruning = commands[command]

			if len(argvs) < len(FVARS[fruning].keys()):
				for key,res in FVARS[fruning].items():
					VARS[key] = res

			for argv_function in r(argvs):
				VARS[list(FVARS[fruning].keys())[argv_function]] = argvs[argv_function]

			for line_in_func in function[commands[command]]:
				com_in_func,*argvs_in_func = line_in_func
				RUN(com_in_func,argvs_in_func)


		else:
			commands[command](argvs)
	else:
		function[fnow].append([com,*argvs])


line_number = -1
funcs = 0
comment = False
out=open(fileout,'w')
with open(filein,"r") as code_file:
	code = code_file.readlines()

	for line in r(code):
		if code[line].find("/*") != -1:
			code[line] = 'NOP /*'
			# code[line] = code[line][code[line].find("/*"):]
			comment = True

		if code[line].find("*/") != -1:
			code[line] = ''
			# code[line] = code[line][:code[line].find("*/")+1]
			comment = False
		if not comment:
			code[line] = clean_line(code[line])
		else:
			code[line] = ''

	# try:
	if True:
		while not line_number >= len(code)-1:
			line_number+=1
			line = code[line_number]
			if not line:continue
			if line == []:break
			com = line.pop(0)
			args = line[0]
			for arg in r(args):
				args[arg] = args[arg].strip()
				# \$ -> $ with no eval or VARS[] stuff
				try:
					if args[arg][0] == '$':

						if args[arg][1:] in VARK():
							args[arg] = VARS[args[arg][1:]]

						else:
							try:
								args[arg] = eval(args[arg][1:])
							except SyntaxError:
								if args[arg].find('"') != -1:
									args[arg] = args[arg][1:]
								# print(f"{color['red']}\n\nError in code Syntax [{args[arg][1:]}] (check for spaces without \){color['nc']}")

					elif args[arg][0:2] == '\$':
						args[arg] = args[arg][1:]

				except IndexError:print(f"{color['light red']}\
little error at line : {line_number+1}\n\
cause:\n\
maybe space in line that already ended or double+ space\n\n\
fix this, fatal errors can occour\
{color['nc']}\
")


			RUN(com,args)

		# pass

# ending file read (safe exit) & show VARS
out.close()
if "--debug" in argk:
	print('##################',end='')
	[print(f"\n{i} : {repr(VARS[i])}",end='') for i in VARK()]
print("\n#### out file ####\n")
ShowFileOut()

exit(VARS["EXT"])
