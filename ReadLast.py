#! /usr/bin/python3.9
# READ ME FIRST

# read everything w/ # at the begining
# after u run this program, there will be a file called "out.txt" (u can change it on line 13)
# if any error occour notify me (msg me on reddit) w/ pics of the problem
# to run this file u must install python 3.8 or 3.9 at https://www.python.org/downloads/
# right click on this file and click "run with python" or something

NameOfFile = "read.txt"
# e.g. NameOfFile = "unicode letters.txt"

with open("out.txt",'w') as OutFile:
	with open(NameOfFile,'r') as file:
		AllLines = file.readlines()
		if AllLines[-1][-1] != '\n':
			AllLines[-1]+='\n'
		for line in AllLines:
			char = line[-2]
			OutFile.writelines(f"{char}\n")

print("done!")
input("press any key to end")