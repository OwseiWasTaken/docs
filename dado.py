#! /usr/bin/python3.9
#imports
from sys import argv
from time import time as tm
from random import randint as rint

def ArgvAssing(argvs:iter) -> dict:
	'''
	this function will loop through all argvs, and will define the ones starting with - as indicators
	and the others just normal arguments
	the returning value will be a dictionary like this:
	argv = ['-i','input','input2','-o','output','output2']
	{'-i':['input','input2],'-o':['output','output2']}
	'''
	# _log.add(f'func ( argv_assing ) with {argvs}')
	indcn=[]
	ret={}
	for i in range(len(argvs)):
		if str(argvs[i])[0] == '-':
			indcn.append(i)

	if indcn == []:
		if argv == []:
			ret[None] = []
		else:
			ret[None] = argvs

	elif indcn[0] > 0:
		ret[None] = argvs[0:indcn[0]]

	for index in range(len(argvs)):
		argvs[index] = argvs[index].replace("/-",'-')

	for i in range(len(indcn)):
		try:
			dif = indcn[i+1]-indcn[i]
			add = argvs[indcn[i]:indcn[i]+dif][1:]
			# for AddIndex in r(add):
				# add[AddIndex] = add[AddIndex].replace("/-",'-')
			ret[argvs[indcn[i]:indcn[i]+dif][0]] = add#argvs[indcn[i]:indcn[i]+dif][1:]
		except IndexError:
			add = argvs[indcn[i]+1:]
			# for AddIndex in r(add):
				# add[AddIndex] = add[AddIndex].replace("/-",'-')
			ret[argvs[indcn[i]]] = add#argvs[indcn[i]+1:]
	return ret


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
