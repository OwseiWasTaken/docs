#! /usr/bin/python3.9
#imports
from util import *


#main
def Main(argv) -> int:
	argk = list(argv.keys())
	def get(*indicators:object) -> list:
		nonlocal argv,argk
		other = []
		for indicator in indicators:
			if indicator in argk:
				for item in argv.get(indicator):
					other.append(item)
		return other

	min = 0
	max = 6
	
	try:
		min = int(get(None)[0])
	except Exception:pass

	try:
		max = int(get(None)[1])
	except Exception:pass

	print(rint(min,max))

	return 0




#start
if __name__ == '__main__':
	argv = ArgvAssing(argv[1:])
	start = tm()
	ExitCode = Main(argv)

	if '--debug' in argv.keys():
		if not ExitCode:printl("%scode successfully exited in " % color["green"])
		else:printl("%scode exited with error %d in " % (color["red"],ExitCode))
		print("%.3f seconds%s" % (tm()-start,color["nc"]))
	exit(ExitCode)
