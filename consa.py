#! /usr/bin/python3.9
#imports
from util import *



#main
def Main(argv):
	argk = list(argv.keys())
	def get(*indicators:object) -> list:
		nonlocal argv,argk
		other = []
		for indicator in indicators:
			if indicator in argk:
				for item in argv.get(indicator):
					other.append(item)
		return other

	ncs = average((get("-NS","-ns","-Ns","-nS","-ncs","-Ncs","-nCs","-ncS","-nc","-NC","-Nc","-nC")),ParseString=True)*.3
	p50 = average(get("-p50","-P50","-p5","-P5"),ParseString=True)*.3
	p100 = average(get("-p100","-P100","-p10","-P10","-p1","-P1"),ParseString=True)*.4
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
