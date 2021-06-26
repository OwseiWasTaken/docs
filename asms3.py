#! /bin/python3.9
from util import *
clear()

# plan
# token oriented
# (means)
# MOV $var NewVar
# tokenized =
# func : MOV | var(int/string/etc) : ($var value) | word : (NewVar)
# funcs[line.func](line.vars)


# file.split_bracket(" ",";")

CommandsList = ["END"
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
,"GET"
]

tokens_and_symbols = {
'+':"PLUS"
,'-':"MINUS"
,'*':"MUL"
,'/':"DIV"
,'(':"LPAREN"
,')':"RPAREN"
,'{':"LKEY"
,'}':"RKEY"
,'[':"LCOL"
,']':"RCOL"
,'=':"EQUAL"
}
class Token:
	def __init__(this,value,type):
		this.value,this.type = value,type
	def __repr__(this):
		return f"{this.value} : {this.type}"

class line:
	def PrevChar(this):
		this.CurrentIndx-=1
		if inrange(this.CurrentIndx,this.Content):
			if this.Content[this.CurrentIndx] in ' \t':
				this.PrevChar()
			else:
				this.CurrentChar = this.Content[this.CurrentIndx]
		else:
			this.CurrentChar = None


	def NextChar(this):
		this.CurrentIndx+=1
		if inrange(this.CurrentIndx,this.Content):
			this.CurrentChar = this.Content[this.CurrentIndx]
		else:
			this.CurrentChar = None

	def lex(this):
		Tokens = []
		Number = False
		this.PrevChar()
		while this.CurrentChar != None and this.NextChar() == None:


			if this.Content[this.CurrentIndx] in ' \t':
				# this.NextChar()
				continue

			elif this.CurrentChar in ['\'','\"']:
				# strings
				Tokens.append(Token(this.MakeString(this.CurrentChar),"string"))
				# continue

			elif this.CurrentChar.isnumeric() or this.CurrentChar == '.':
				# numbers
				Tokens.append(Token(this.MakeNumber(),"number"))
				# continue

			elif this.CurrentChar in tokens_and_symbols.keys():
				# symbols
				Tokens.append(Token(tokens_and_symbols[this.CurrentChar],"symbol"))
				# continue

			elif this.CurrentChar in '%':
				# vars
				Tokens.append(Token(this.MakeVar(),"var"))
				# continue

			else:
				# commands
				command = this.Content[this.CurrentIndx:this.CurrentIndx+3]
				if command in CommandsList:
					Tokens.append(Token(command,"command"))
					this.NextChar()
					this.NextChar()
				# continue


			print(f"c:{this.CurrentChar} @ {this.CurrentIndx}")




		return Tokens

	def MakeVar(this):
		ret = ""
		while this.NextChar() == None and not this.CurrentChar in [None,' \t\n',tokens_and_symbols.keys()]:
			ret+=this.CurrentChar
			# this.NextChar()
		return ret[1:]


	def MakeString(this,StartingQout):
		RetString = StartingQout

		while this.NextChar() == None and this.CurrentChar != None:
			RetString+=this.CurrentChar
			if this.CurrentChar == StartingQout:
				return RetString



	def MakeNumber(this):
		num_str = ''
		dot_count = 0

		while this.CurrentChar != None and (this.CurrentChar.isnumeric() or this.CurrentChar=='.'):
			if this.CurrentChar == '.':
				if dot_count:
					raise SyntaxError(f"\nerror on making number {this.Content} <- second dot (.) found")
				else:
					dot_count += 1
					num_str += '.'
			elif this.CurrentChar.isnumeric():
				num_str+=this.CurrentChar
			this.NextChar()

		if dot_count:
			value = eval(num_str)

		return num_str



	def __init__(this,line):
		this.Content = line
		this.CurrentChar = ''
		this.CurrentIndx = -1
		this.NextChar()

a = line("MOV  '5' %VAR")
print(a.lex())