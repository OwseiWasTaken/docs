#! /usr/bin/python3.9
#imports
from util import *


#main
def Main() -> int:
	HideCursor()


	# DA RULES

	# minus one | - | VARS[POINTER] = VARS.get(POINTER,0)-1
	# plus one | + | VARS[POINTER] = VARS.get(POINTER,0)+1
	# move pointer right | > | POINTER+=1
	# move pointer left | < | POINTER-=1
	# print char | . | printl(VARS[POINTER])
	# get char | , | VARS[POINTER] = ord(GetCh())
	# loop | [ ... ]
	# MAKR = CodeLine; do stuff (...) when in ] check if VARS[POINTER], if false, move on, if true, CODE = MARK
	# (MY RULES)
	# random bool | * | VARS[POINTER] = rbool()
	# exit | $ | exit(VARS[POINTER])


	FileName = get("-i","-f","--file","--input").first
	if FileName == None:
		print("brainfuck.py needs an input file (-i, --input, -f, --file")
	with open(FileName) as FileObj:
		FileData = FileObj.readlines()
	# got file's lines

	# set vars
	VARS = {0:0}
	POINTER = 0
	col = 0
	char = ''
	out = ''
	tick = 0
	GOTO = 0
	ExitCode = 0

	AllInOne = get("--debug", "-D").bool
	PrintTick = get("--PrintTick", "-PT").exists
	verbose = get("--verbose", "-V").bool


	if verbose:
		explains = {
			'<':"moves the pointer left",
			'>':"moves the pointer right",
			'+':"adds one to the cell the pointer is pointing",
			'-':"subtracts one to the cell the pointer is pointing",
			'[':"jumps to the next ] if the current cell the pointer is pointing is zero",
			']':"jumps to the previous [ if the current cell the pointer is pointing is zero",
			',':"get's input and stores it in the current cell the pointer is pointing",
			'.':"prints the current cell the pointer is pointing",
		}

	x, _ = GetTerminalSize()
	x+=11
	marks = [',', '.', '>', '<', '+', '-', '[', ']', '*', '$']

	def debug():
		# print memory tape
		tape = ''
		for index in r(VARS.values()):
			thing = str(VARS[index])
			if index == POINTER:
				tape += color["br red"]+thing+color["nc"]+', '
			else:
				tape += thing+', '
		tape = tape[:-2]

		# if tape is too big print ccell
		if len(tape) > x:
			tape = color["br red"] + str(VARS[POINTER]) + color["nc"]

		# print tape
		ClearLine(0)
		print(f"{pos(0,0)}{tape}")

		# print symb explanation
		if verbose:
			ClearLine(1)
			print(f"{pos(1,0)}{char} : {explains[char]}")
		else:
			ClearLine(1)
			tape = ""
			for vr in r(VARS.values()):
				ch = repr(chr(VARS[vr]))[1:-1]
				if vr == POINTER:
					tape += color["br red"] + ch + color["nc"] + ', '
				else:
					tape += ch + ', '

			tape = tape[:-2]
			if len(tape) > x:
				tape = color["br red"] + repr(chr(
					VARS[POINTER]
				)) + color["nc"]
			print(tape)



		# print debug line
		ClearLine(3)
		print(f"{pos(3,0)}pos {col}, ->: {POINTER}, tick: {tick}, goto:{GOTO} out: {repr(out)}")

		# print code + highlight current char
		ClearLine(4)
		printl(pos(4,0))
		CodeLines = ""
		for i in r(CODE):
			if col == i:
				CodeLines += COLOR.BrRed+CODE[i]+COLOR.nc
			else:
				CodeLines += CODE[i]
		printl(CodeLines)

		# step-by-step debug
		return GetCh()

	# make single-line code
	CODE = "".join([x for x in "".join(FileData) if x in marks]).replace("DNL","\n")
	# make [] loop
	StartMarks, EndMarks = {},{}
	ToEnd = []
	while col < len(CODE):
		char = CODE[col]
		if char == '[':
			ToEnd.append(col)

		elif char == ']':
			start = ToEnd.pop(-1)
			StartMarks[start] = col
			EndMarks[col] = start
			


		col+=1

	col = 0
	clear()
	# main loop
	while col < len(CODE):
		char = CODE[col]
		if AllInOne and tick>GOTO-1:
			dbchar = debug()
			if dbchar == ':':
				#ClearLine(_-2,start=COLOR.BkGrey)
				ShowCursor()
				GOTO = GetInt(f'{pos(_,0)}:',excepts = [''] , default=0)
				HideCursor()
				clear()
				# col -= 1
				continue

			if dbchar == 'q':
				return 0

		if char == ',':
			if AllInOne:#AllInOne = DebugMode
				printl(pos(_,0)+':')
			VARS[POINTER] = ord(GetCh())
		elif char == '.':
			if not AllInOne:
				printl(chr(VARS[POINTER]))
			out+=chr(VARS[POINTER])
		elif char == '>':
			POINTER += 1
			if not POINTER in VARS.keys():
				VARS[POINTER] = 0 
		elif char == '<':
			POINTER -= 1
			if POINTER < 0:
				ShowCursor()
				raise ValueError(f"\n\n{color['br red']}POINTER can't be negative!")
			if not POINTER in VARS.keys():
				VARS[POINTER] = 0
		elif char == '+':
			num = VARS.get(POINTER,0)+1
			if num > 255:
				num = 0
			VARS[POINTER] = num
		elif char == '-':
			num = VARS.get(POINTER,0)-1
			if num < 0:
				num = 255
			VARS[POINTER] = num
		elif char == '[':
			if VARS.get(POINTER) == 0:
				col = StartMarks[col]
		elif char == ']':
			if VARS.get(POINTER):
				col = EndMarks[col]
		elif char == '*':
			VARS[POINTER] = int(rbool())
		elif char == '$':
			col = len(CODE)
			ExitCode = VARS[POINTER]
		col+=1
		tick += 1
	# debug()
	if AllInOne:
		clear()
		printl(out)
	if PrintTick:
		print(f"\n\n{tick}")
	return ExitCode






#start
if __name__ == '__main__':
	start = tm()
	try:
		ExitCode = Main()
	except KeyboardInterrupt:
		ExitCode = 130
	ShowCursor()
	exit(ExitCode)
