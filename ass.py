#! /usr/bin/python3.9
#imports
from util import *
#"ASsembly Super"
#main
def main(argv):
	man = False
	if "-man" in argv.keys():
		if argv["-man"]:
			ss("clear")
			print("""
			"STT" = exit status
			"ACC" = easy access accumulator
				with commands
				"ADD"
				"SUB"
				"MUL"
				"DIV"
			""
			""")
	rf = False
	if "-rf" in argv.keys():
		rf = eval(lst1(argv["-rf"]))
	stdin = ""
	if "-s" in argv.keys():
		stdin = lst1(argv["-s"])
	filein = lst1(argv['-i'])
	fileout = "out.txt"
	if "-o" in argv.keys():
		fileout = lst1(argv["-o"])
	PRT = log(tm=False)
	PRT.LOG=[]
	PRT.add(f"in    : {filein}")
	PRT.add(f"stdout: {fileout}")
	PRT.add(f"stdin : {stdin}")
	PRT.add(f"##################")
	PRT.add("\\/\\/ out file \\/\\/")
	with open(filein,'r') as file:
		if stdin:
			with open(stdin,'r') as stdinfile:
				stdin=stdinfile.read().split('\n')
		#program vars
		VAR = {
		 "STT":0
		,"ACC" : 0
		,"DAT" : None
		,"FLG" : False
		,"MKS" : {}
		,"MMR" : 0
		}
		print("##################")
		try:
			with open(fileout,'w') as out:
				fls = file.readlines()
				l = -1
				try:
					while True:
						l+=1
						line = fls[l]
						if line[0] == "!":
							VAR["MKS"][line[:-1]] = l
				except IndexError:pass
				l = -1
				# print(fls)
				while True:
					ad=""
					adr=""
					ad2=""
					ad2r=""
					l+=1
					try:
					# if 1:
						line = fls[l][:-1]
					except IndexError:
						if not "END" in file.read():
							print(f"{color['red']}Syntax Error (254) no \"END\" command {color['nc']}")
							VAR["STT"] = 254
							break
					#"interpreter" part
					if line == "":continue
					if line == '\n':continue
					# if line[0] == "!":VAR["MKS"][line] = l
					if line[0] == ';':continue
					if line[0] == "\t":
						line = line[1:]
					# 
					if line[0] == '+':
						if VAR["FLG"]:
							line = line[1:]
						else:
							continue
					#
					elif line[0] == '-' :
						if not VAR["FLG"]:
							line = line[1:]
						else:
							continue
					K = line.split()
					try:
					# if 1:
						ad0 = K.pop(0)
						# ad
					# 
						ad = K[0:-1]
						adr = "".join(ad)
						ad = " ".join(ad)
						if ad:
							if ad in VAR.keys():
								ad = VAR[ad]
							else:
								if ad.isnumeric():
									while ad[0] == '0' and len(ad) != 1:
										ad = ad[1:]
								if ad[0] != "!":
									ad = eval(ad)
					except IndexError:pass
					# 
					# ad2
					try:
					# if 1:
						try:
							ad2 = K[-1]
							ad2r = ad2
							if ad2 in VAR.keys():
								ad2 = VAR[ad2]
							else:
								if ad2.isnumeric():
									while ad2[0] == '0' and len(ad2) != 1:
										ad2 = ad2[1:]
								if ad2[0] != "!":
									ad2 = eval(ad2)
						except NameError:
							VAR[ad2] = None
							ad2 = VAR[ad2]
					except IndexError:pass
					try:
					# if 1:
						if not ad and ad2:
							ad = ad2
							adr = ad2r
					except UnboundLocalError:pass
					if rf:
						print(f"{l} : {line}")
					# commands = {"NOP":lambda:pass
					# ,"INW":VAR["INR"] = str(stdin.pop(0))
					# ,"MVV":VAR[ad2] = VAR[ad]
					# ,"ADD":
					# }
					# 
					if "INW" == ad0:
						VAR["INR"] = str(stdin.pop(0))
					elif "MOV" == ad0:
						VAR[ad2r] = ad
					elif "ADD" == ad0:
						VAR["ACC"] += float(ad2)
					elif "SUB" == ad0:
						VAR["ACC"] -= float(ad2)
					elif "SET" == ad0:
						VAR["ACC"] = float(ad2)
					elif "MUL" == ad0:
						VAR["ACC"] *= float(ad2)
					elif "DIV" == ad0:
						VAR["ACC"] /= float(ad2)
					elif "SAV" == ad0:
						VAR["DAT"] = ad2
					elif "LOD" == ad0:
						VAR[ad2r] = VAR["DAT"]
					elif "EXT" == ad0:
						if int(ad2) > 255:
							print(f"/\\/\\ Syntax Error (253) at line {l} EXT argument bigger than 255")
							VAR["STT"] = 253
							break
						VAR["STT"] = int(ad2)
					elif "END" == ad0:
						break
					elif "PRT" == ad0:
						if ad == '':
							print(f"Error (252) at line {l} undefined var to PRT")
							VAR["STT"] = 252
							break
						PRT.add(ad)
						out.write(f"{ad}\n")
					elif "JMP" == ad0:
						l = VAR["MKS"][ad]
					elif "SLP" == ad0:
						sleep(seg=float(ad))
					elif "NOP" == ad0:pass
					elif "FLG" == ad0:
						VAR["FLG"] = bool(ad)
					elif "EQU" == ad0:
						VAR["FLG"] = (ad==ad2)
					elif "JIN" == ad0:
						VAR[adr] = "".join(ad + ad2)
					elif "TST" == ad0:pass
					elif "DEL" == ad0:
						VAR.pop(adr)
						#VAR[adr] = None
					elif "CHR" == ad0:
						VAR[adr] = chr(int(ad2))
					elif "ORD" == ad0:
						VAR[adr] = ord(ad2)
					# 
					elif "ADV" == ad0:
						# print(VAR)
						# print(adr)
						# print(f"{VAR[ad2r]}")
						VAR[ad2r] += float(ad)
					elif "SBV" == ad0:
						VAR[ad2r] -= float(ad)
					elif "MLV" == ad0:
						VAR[ad2r] *= float(ad)
					elif "DVV" == ad0:
						VAR[ad2r] /= float(ad)
					elif "CLS" == ad0:
						ss('clear')
					elif "PRT_VAR" == ad0:
						for i in VAR.keys():
							PRT.add(f"{i} : {VAR[i]}")
							out.write(f"{i} : {VAR[i]}\n")
					elif "MEM" == ad0:
						X = sizeof(VAR[ad2r])
						if ad2:
							PRT.add(X)
							out.write(str(X))
						else:
							PRT.add(X)
							out.write(str(X))
						VAR["MMR"] = X
					# elif "SEL" == ad0 add num
					# add = add[num]
					# else:
					# 	print('/\\/\\')
					# 	print(f"{color['red']}Syntax Error (255) at line {l}{color['nc']}")
					# 	VAR["STT"] = 255
					# 	break
		except KeyboardInterrupt:
			pass
		# 
		if rf:
			print("##################")
		for i in VAR.keys():
			print(f"{i} : {repr(VAR[i])}")
		print("##################")
		PRT.show()
		print("##################")
	return VAR["STT"]
# 
#start
if __name__ == '__main__':
	start = tm()
	name = argv.pop(0)
	if (debug:='--debug' in argv):
			argv.remove('--debug')
	ss("clear")
	# exit_code = main(argv_assing(argv))
	# 
	if debug:
		if not exit_code:
			print(f'code successfully exited in ',end='')
		else:
			print(f'code exited with error {exit_code} in ',end='')
		print(f'{round(tm()-start,5)} seconds')
	exit(exit_code)