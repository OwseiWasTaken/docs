#! /usr/bin/python3.8
#imports

# todo:
# if ',' in line:
# change global vars from defs to loval vars
# remove local vars from defs
# ret to make local var global
# ret VAA ;as; VBB
# /\ make VAA$ (local) into VBB (global)
from util import *


#main
def main(argv):
	functype = type(lambda:0)
	rf = False
	rbool = bool(rint(0,1))
	if "-rf" in argv.keys():
		rf = eval(lst1(argv["-rf"]))
	stdin = ""
	if "-s" in argv.keys():
		stdin = lst1(argv["-s"])
	filein = lst1(argv['-i'])
	fileout = "out.txt"
	if "-o" in argv.keys():
		fileout = lst1(argv["-o"])
	if stdin:
		with open(stdin,'r') as stdinfile:
			stdin=stdinfile.read().split('\n')
	Log=log(tm=False)
	Log.LOG = []
	Log.add(f"in    : {filein}")
	Log.add(f"stdout: {fileout}")
	Log.add(f"stdin : {stdin}")
	Log.add('')
	if rf:
		Log.add(f"##################")
		Log.add("\\/\\/ out file \\/\\/")
		print("##################")
	FVARS = {}
	VAR = {
		 "STT" : 0
		,"FLG" : False
		,"MKS" : {}
		,"ACC" : 0
	}

	with open (filein,'r') as file:
		with open(fileout,'w') as out:
			fls = file.readlines()
			l = -1
			funcs = 0
			try:
				while True:
					l += 1
					line = fls[l][:-1]
					while line[0] == " ":
						fls[l] = [fls][l][1:]
						line=fls[l]
					if line[0] == '\t':
						fls[l] = line[1:]
						line = fls[l]
					if line[:2] == '  ':
						fls[l] = line[2:]
						line = fls[l]
					if line[-1] == "!":
						VAR["MKS"][line] = l
					if line == "":continue
					if line == "\n":continue
					for i in r(line):
						if line[i] == ';' or (line[i-1:i] == '//' and i-1 > 0):
							fls[l] = line[:i]
					if line[:3] == "DEF":funcs+=1
					if line[:3] == "END":
						if funcs:
							funcs-=1
						else:
							break
			except IndexError:pass

			def INW(adr=[None]):
				adr=lst1(adr)
				if adr == None:
					adr = "INR"
				if len(stdin) == 0:
					VAR[adr] = "FILE_ENDED"
				else:
					VAR[ adr ] = stdin.pop(0)
				return 0

			def MOV(val):
				if len(val) in [3,4]:
					if val[-1] == "RNG":
						adr = val.pop(2)
						for i in r(val):
							if val[i] in VARK:
								if not VAR[val[i]] == None:
									val[i] = VAR[ val[i] ]
						R=rint(
								min([float(val[0]),float(val[1])]),
								max([float(val[0]),float(val[1])])
							)
						VAR[adr] = R
						return 0


				adr = None
				if len(val) == 2:
					val,adr = val
				else:
					val = val[0]
				if adr == None:
					val,adr = adr,val
				if val in VARK:
					val = VAR[ val ]

				VAR[ adr ] = val
				return 0

			def ADD(val):
				adr = None
				if len(val) == 2:
					val,adr = val
				else:
					val = val[0]
				if adr == None:
					adr = "ACC"
				if val in VARK:
					val = VAR[ val ]
				try:
					VAR[adr]+=float(val)
				except TypeError:
					if VAR[adr] == None:
						VAR[adr] = val
					else:
						VAR[adr] = f"{VAR[adr]}{val}"
				return 0
			def SUB(val):
				adr = None
				if len(val) == 2:
					val,adr = val
				else:
					val = val[0]
				if adr == None:
					adr = "ACC"
				if val in VARK:
					val = VAR[ val ]
				# print(repr(val),repr(adr))
				# try:
				VAR[adr]-=float(val)
				# except TypeError:
					# VAR[adr] = -val				
				return 0
			def DIV(val):
				adr = None
				if len(val) == 2:
					val,adr = val
				else:
					val = val[0]
				if adr == None:
					adr = "ACC"
				if val in VARK:
					val = VAR[ val ]
				try:
					VAR[adr]/=float(val)
				except KeyError:
					VAR[val]/=adr
				return 0
			def MUL(val):
				adr = None
				if len(val) == 2:
					val,adr = val
				else:
					val = val[0]
				if adr == None:
					adr = "ACC"
				if val in VARK:
					val = VAR[ val ]
				VAR[adr]*=float(val)
				return 0
			def EXT(val):
				val=lst1(val)
				if val in VARK:
					val = VAR[ val ]
				if int(val) > 255:
					print(f"/\\/\\ Syntax Error (253) at line {l+1} EXT argument bigger than 255")
					return 253
				VAR["STT"] = val
				return 0
			def PRT(val):
				nonlocal out
				# for i in r(val):
					# if val[i] in VARK:
						# val[i] = VAR[ val[ i ] ]
				if val == [None]:
					Log.add("\n")
					out.write("\n\n")
					return 0
				try:
					val=" ".join(val)
				except TypeError:
					val = lst1(val)
				Log.add(str(val))
				out.write(f"{val}\n")
				return 0
			def JMP(val):
				nonlocal l
				val = lst1(val)
				if val[-1] != "!":
					val = val+"!"
				if val in VARK:
					val = VAR[val]
				l=VAR["MKS"][val]

				return 0
			def SLP(val):
				sleep(seg=float(lst1(val)))
				return 0


			def EQU(val):
				VAR["FLG"] = eval(" ".join([str(v) for v in val]))
				# for i in r(val):
				# 	if val[i] in VARK:
				# 		val[i] = VAR[ val[ i ] ]
				# F=True
				# for i in val:
				# 	for ii in val:
				# 		if i!=ii:
				# 			F=False
				# VAR["FLG"] = F
				return 0
			def NOP(*val):
				return 0
			def ORD(val):
				val,adr = val
				if val in VARK:
					val = VAR[ val ]
				VAR[ adr ] = ord(val)
				return 0
			def CHR(val):
				val,adr = val
				if val in VARK:
					val = VAR[ val ]
				VAR[ adr ] = chr(int(val))
				return 0
			def DEL(val):
				for i in val:
					VAR.pop(i)
				return 0
			def CHG_STD_OTF(val):
				nonlocal out
				out = open(val[0],'w')
				return 0
			def CHG_STD_INF(val):
				nonlocal stdin
				if type(lst1(val)) != list:
					with open(lst1(val),'r') as stdinfile:
						stdin=stdinfile.read().split('\n')
				return 0
			def OSC(val):
				val = " ".join(val)
				if val[:2] == "cd":
					cd(val[3:])
				else:
					ss(val)
				return 0
			def EXS(val):
				if type((val:=lst1(val))) != list:
					if val in VARK:
						VAR["FLG"] = True
				else:
					val,adr = val
					VAR[ adr ] = val in VARK
				return 0
			# def MEM(val):
			def mem(var,a=0):
				for vrs in var:
					for i in lst1(vrs.keys()):
						if type(vrs[i]) == dict:
							a+=mem(vrs[i])
						a+=sizeof(vrs[i])
				return a

			function,fnow = {},None
			def DEF(val):
				nonlocal function,commands,fnow,FVARS
				fname = val.pop(0)
				commands[fname] = NOP
				function[fname]=[]
				fnow = fname
				FVARS[fname]=val


			def KIL(val):
				for i in val:
					ss(f"pkill {lst1(i)}")




			def RUN(line):
				nonlocal fnow,rbool
				com,*args = " ".join(split_bracket(line,","," ")).split()
				# com,*args = line.split()
				# com = com[:-1]
				# args = [a[:-1] for a in args]				
				if com[-1] == "!":
					return 0
				if not fnow:
					try:
						for i in r(args):
							while args[i] == "<<":
								args.pop(i)
							if args[i][-1] in ["f","F"]:
								args[i] = float(args[ i ][ :-1 ] )
							if args[i][-1] in ["i","I"]:
								args[i] = int(	args[ i ][ :-1 ] )
							if args[i][-1] == "$" and type(commands[com])!=list:
								try:
									args[i] = VAR[ args[i][:-1] ]
								except KeyError:
									args[i] = eval( args[ i ][ :-1 ] )
					except IndexError:pass
				argp = [f'{i}' for i in args]
				if rf:
					if fnow:
						print(f'{fnow} : {l+1} : {com} {" ".join(argp)} ')
					else:
						print(f'{l+1} : {com} {" ".join(argp)} ')
				if com == "END\n":
					com = "END"
				
				# print(f'{repr(com)} : {repr(args)}')
				cm = commands[com]

				if com == "END":
					if fnow != None:
						commands[fnow] = function[fnow]
						VAR[fnow] = function[fnow]
						fnow = None
					else:
						return "END"
				elif fnow:
					function[fnow].append([com,*args])
				
				elif type(cm) == list:
					FVARSVAL = list(FVARS.values())[0]
					for i in r(args):
						try:
							VAR[FVARSVAL[i]] = eval(args[i])
						except NameError:
							 VAR[FVARSVAL[i]] = args[i]
					for i in r(cm):
						for ii in r(cm[i]):
							cm[i][ii] = str(cm[i][ii])
						k = " ".join(cm[i])
						RUN(k)
				
				
				
				elif type(cm) == functype:
					if cm(args):
						return 1

			commands = {"END":NOP
			,"NOP":NOP
			,"MOV":MOV
			,"ADD":ADD
			,"SUB":SUB
			,"MUL":MUL
			,"DIV":DIV
			,"EXT":EXT
			,"PRT":PRT
			,"JMP":JMP
			,"SLP":SLP
			,"EQU":EQU
			,"INW":INW
			,"ORD":ORD
			,"CHR":CHR
			,"DEL":DEL
			,"":NOP
			,"!":NOP
			,"\n":NOP
			,"OSC":OSC
			,"EXS":EXS
			,"CHO":CHG_STD_OTF
			,"CHI":CHG_STD_INF
			,"DEF":DEF
			,"KIL":KIL
			,"MEM":mem
			,"RNG":RNG
			}

			l=-1
			try:
				VARK = VAR.keys()
				while True:
					l+=1
					try:
						line = fls[l]
					except IndexError:
						print("WARNING no END command detected at end of file")
						break
					if line == "":continue
					if line[0] == " ":continue
					if line[0] == ";":continue
					if line[0:2] == "//":continue
					if line[0] == "\n":continue
					if line[0] == "!":continue
					try:
						line = fls[l]#[:-1]
					except IndexError:
						print(f"{color['red']}Syntax Error (254) no \"END\" command {color['nc']}")
						VAR["STT"] = 254
						break
					#
					try:
						if line[0] in ['-','+']:
							if VAR["FLG"]:
								if line[0] == '+':
									line = line[1:]
								else:
									continue
							else:
								if line[0] == '-':
									line = line[1:]
								else:
									continue
					except IndexError:pass
					# try:
					RVAR = RUN(line)
					if RVAR in ["END",1]:
						break

			except KeyboardInterrupt:pass
			#################################
			if rf:print(f'{l+1} : END')
			print("##################")
			Log.show()
			print("##################")
			[print(f"{i} : {repr(VAR[i])}") for i in VARK]
			print("##################")
		out.close()




	return 0

#start
if __name__ == '__main__':
	start = tm()
	name = argv.pop(0)
	if (debug:='--debug' in argv):
			argv.remove('--debug')
	ss("clear")
	exit_code = main(argv_assing(argv))

	if debug:
		if not exit_code:
			print(f'code successfully exited in ',end='')
		else:
			print(f'code exited with error {exit_code} in ',end='')
		print(f'{round(tm()-start,5)} seconds')
	exit(exit_code)
