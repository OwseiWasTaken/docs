#! /usr/bin/python3.9
#imports
from util import *


#main
def Main(argv):
	argk = list(argv.keys())
	def	get(*indicators,DoEval=False,OnlyOne=False):
		nonlocal argv,argk
		other = []
		for indicator in indicators:
			if indicator in argk:
				other.append(argv[indicator])
		if OnlyOne:
			return other[0]
		else:
			return other

	ncs = average(get("-ncs","-Ncs","-nCs","-ncS","-nc","-NC","-Nc","-nC"),ParseString=True)*.3
	p50 = DeepSum(get("-p50","-P50","-p50","-P50","-p5","-P5","-p"),ParseString=True)*.3
	p100 = DeepSum(get("-p100","-P100","-p10","-P10","-p1","-P1","-P"),ParseString=True)*.4
	print(round(ncs+p50+p100,5))
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
