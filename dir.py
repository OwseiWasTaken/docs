#! /usr/bin/python3.9
#imports
from util import *

root = {
	'/':{}
}
# dir : dict
# file : str (w/ eval)

def AddDir(name,Path):
	# path = list
	# name = str
	Path = Path.split('/')
	for PathIndex in r(Path):
		Path[PathIndex] = f'{Path[PathIndex]}/'
	Path.pop(-1)
	if name[-1] != '/':
		name+='/'
	contents = '{}'
	dir = ''.join([f"[\"{di}\"]" for di in Path])
	exec(f"root{dir}[\"{name}\"] = {contents}")

def AddFile(name,content,Path):
	# path = list
	# name = str
	# dir = ''.join([f"[\"{di}\"]" for di in path])
	Path = Path.split('/')
	for PathIndex in r(Path):
		Path[PathIndex] = f'{Path[PathIndex]}/'
	
	Path.pop(-1)
	
	Path =  ''.join([f"[\"{dir}\"]" for dir in Path])
	name = repr(name)
	exec(f"root{Path}[{name}] = \"{content}\"")

def ls(Dict,Deep=0,rec=False,UltraRec=False):
	rec = bool(rec+UltraRec)
	# go into dict
	# show contents as dir/ and file
	# ├─
	for Key in Dict.keys():
		if type(Dict[Key]) != dict:
			print(f"{'├ '*Deep}{Key}")
		else:
			print(end=color["light blue"])
			if rec:
				print(f"{'├ '*Deep}{Key}:")
				ls(Dict[Key],Deep=Deep+1,rec=UltraRec,UltraRec=UltraRec)
			else:
				print(f"{'├ '*Deep}{Key}")
			print(end=color["nc"])

def lsPath(Path,cat=False,rec=False,UltraRec=False):
	if type(Path) == str and not cat:
		Path = Path.split('/')
	for PathIndex in r(Path):
		if Path[PathIndex][-1] != '/' and not cat:
			Path[PathIndex] += '/'

	# Path.pop(-1)
	Path = ''.join([f"[\"{dir}\"]" for dir in Path])

	Path = eval(f"root{Path}")
	# print(Path)
	if cat:
		ShowFile(Path)
	else:
		ls(Path,rec=rec,UltraRec=UltraRec)

def ShowFile(file):
	print(file)


path = ['/']
user = "owsei"
commands = {
	"ls":lsPath
	,"l":lsPath
	,"cat":ShowFile
}

AddDir("home/",'/')
AddDir(user,'/home/')
AddDir("Documents",f'/home/{user}')
AddDir("Desktop",f'/home/{user}')
AddDir("Downloads",f'/home/{user}')
AddDir("Templates",f'/home/{user}')

AddFile(".bashrc","passwd : 123",f"/home/{user}/")
#main
def main(argv):
	
	path.append("home/")
	path.append("owsei/")

	fl = path
	
	fl.append(".bashrc") 
	lsPath(path,cat=True)


	return 0;


# start
exit(main(argv_assing(argv)))