#! /usr/bin/python3.9
#imports
from util import *

points = 0

class Question(object):
	def __init__(self,Question:str,Answears:list,RightAnwsear:int,points=1):
		self.Question,self.Answears,self.RightAnwsear,self.points = Question,Answears,RightAnwsear,points
	def __call__(self) -> None:
		clear()
		global points
		Question,Answears,RightAnwsear = self.Question,self.Answears,self.RightAnwsear

		# print question and answears
		print(Question)
		print(end=f'{color["yellow"]} | {color["nc"]}')
		for answear in r(Answears):
			print(f"{answear+1}: {color['br magenta']}{Answears[answear]}",end=f'{color["yellow"]} | {color["nc"]}')
		print(":",end='')

		# get input
		UserAnswear = int(input())

		# ret true or false
		if inrange(UserAnswear-1,Answears):
			if self.Answears[UserAnswear-1] == RightAnwsear:
				points+=self.points
		else:
			print(f"\nno answear {UserAnswear-1}\n press enter to continue")
			input()
			self()



questions = [
Question(
#question quote
"what is the biggest country?",
#possible answs
["Brazil","Russia","United states","China"],
#right answ (value not index)
"Russia"

),Question(

"7+2*4",
[36,34,27,17,15],
15

),Question(

"end the frase \"i think therefore\"",
["i am alive","i become","i am","i exist","i am here"],
"i exist",
points=2
)
]


for quest in questions:
	quest()

print(points)
