#! /usr/bin/python3.9
#imports
from util import *

class TerminalMap:
	def __init__(this):
		this.size = this.SetNewSize()
		this.MakeMap()
		this.stats = "nothing..."
	
	def MakeMap(this):
		this.map = [[' ' for x in r(this.x)] for y in r(this.y)]

	def SetNewSize(this):
		this.size = GetTerminalSize()
		this.size=(this.size[0],this.size[1]-1)
		this.x,this.y = this.size
	
	def DrawStr(this,x,y,msg):
		for index in r(msg):
			k = msg[index]

			if k in ['\n',]:#may cause shit if repr() is not use
				k = repr(k)

			this.map[y][x+index] = k

	def DrawCh(this,x,y,ch):
		if len(ch) == 1:
			this.map[y][x] = ch
		else:
			raise ValueError(f"len of ch at TerminalMap.DrawCh(x:{x},y:{y},ch:{cg}) is not 1 : {len(ch)}")
	
	def DrawMap(this):
		for y in r(this.map):
			if this.map[y] == [' ' for x in r(this.x)]:
				this.map[y]=''
		this.draw = 0
		clear()
		for y in r(this.map):
			print()
			if this.map[y] == '':
				continue
			else:
				this.draw+=1
				for x in r(this.map[y]):
					printl(this.map[y][x])
		this.stats+=str(this.draw)
		printl(this.stats)
		return 0



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
		this.map = TerminalMap()


	def Main(this):
		x,y = 0,0
		ch = GetCh()
		while True:
			if ch == 'w' and y:
				y-=1
			elif ch == 's':# and y<this.map.size[0]-2:
				y+=1
			elif ch == 'a' and x:
				x-=1
			elif ch == 'd':# and x<this.map.size[1]-1:
				x+=1

			# draw part
			this.map.MakeMap()
			this.map.DrawCh(x, y, '@')
			this.map.DrawMap()
			this.map.stats = f"|x:{x}|y:{y}|"




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
