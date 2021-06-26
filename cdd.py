#! /usr/bin/python3.9
#imports
from util import *


#main
docs = ls("/home/owsei/Documents")
Doc = []
for i in r(docs):
	if docs[i][-1] == '/' and len(docs[i]) == 3:
		Doc.append(f"{docs[i][:-1]}d")
for i in Doc:
	print(f"alias {i} \"cd /home/owsei/Documents/{i[0:-1]}\"")
