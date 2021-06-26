#! /usr/bin/python3.9
#imports
from util import *

def pos(x:int,y:int) -> str:
	return "\x1B[%i;%iH" % (y,x)

def printf(x:int,y:int,string:str):
	sout.write("%s%s" % (pos(x,y),string))



#main
def Main(argv):
	argk = list(argv.keys())
	def	get(indicators):
		nonlocal argv,argk
		other = []
		for indicator in indicators:
			if indicator in argk:
				other.append(argv[indicator])
		return other
	
	printf(3,3,"hi")
	sleep(7)




	return 0






#start
if __name__ == '__main__':
	argv = ArgvAssing(argv[1:])
	start = tm()
	ExitCode = Main(argv)

	if '--debug' in argv.keys():
		if not ExitCode:printl("%scode successfully exited in " % color["green"])
		else:printl("%scode exited with error %d in " % (color["red"],ExitCode))
		print("%d seconds%s" % (round(tm()-start,5),color["nc"]))
	exit(ExitCode)
