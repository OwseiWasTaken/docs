#! /usr/bin/python3.9
#imports
from util import *

#main
class program:
	def __init__(this):
		# declare CONSTS and argv/argk

		# the three vars that can be initialized now
		this.nums = [2,4,10,12,18,20,30,36,38,48,54,56,70,80,86,88,102,112,118]
		this.resps = {2:'s',6:'p',10:'d',14:'f'}
		this.cons = {'s':0,'p':1,'d':2,'f':3}

	def main(this):
		nums = this.nums
		for num in r(nums):
			if num:number = nums[num]-nums[num-1]
			else:number = nums[num]
			res = this.resps[number]
			this.cons[res]+=1
			print(f"{nums[num]}{' '*(3-len(str(nums[num])))}||{this.cons[res]}{res}{NumberToExponent(number)}")
		return 0

#start
if __name__ == '__main__':
	exit_code = program().main()
	exit(exit_code)
