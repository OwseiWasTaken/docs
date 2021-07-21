#! /usr/bin/python3.9
#imports
from util import *
from ClockLib import n1,n2,n3,n4,n5,n6,n7,n8,n9,n0
import datetime
#main

class Program:
	@property
	def hour(this):
		return list(this.time.hour)
	@property
	def min(this):
		return list(this.time.min)

	def __init__(this,argv):
		# declare vars
		this.argv = argv
		this.argk = list(argv.keys())
		this.bdp = BDP("clock.py")

		try:
			this.col = ' '.join(this.argv["-c"])
			print(color[' '.join(this.argv["-c"])])
			this.bdp.save(color[' '.join(this.argv["-c"])])
		except KeyError:
			print(this.bdp.load())

		if '-r' in this.argk:
			if this.argv['-r'] == []:
				this.rainbow = True
			else:
				this.rainbow = eval(lst1(this.argv['-r']))
		else:
			this.rainbow = False


		this.time = time
		this.weekdays = ["segunda","terça","quarta","quinta","sexta","sábado","domingo"]
		this.numbers={
		'1':n1,'2':n2,'3':n3,'4':n4,'5':n5,'6':n6,'7':n7,'8':n8,'9':n9,'0':n0
		}
		this.LastTime = this.min


		this.colors = ['\x1b[0m'
		,'\x1b[0m'
		,'\x1b[0;31m'
		,'\x1b[0;32m'
		,'\x1b[0;33m'
		,'\x1b[0;34m'
		,'\x1b[0;35m'
		,'\x1b[0;36m'
		,'\x1b[0;37m'
		,'\x1b[0;37m'
		,'\x1b[0;90m'
		,'\x1b[0;90m'
		,'\x1b[0;91m'
		,'\x1b[0;92m'
		,'\x1b[0;93m'
		,'\x1b[0;94m'
		,'\x1b[0;95m'
		,'\x1b[0;96m'
		,'\x1b[0;37m'
		,'\x1b[0;37m'
		,'\x1b[0;91m'
		,'\x1b[0;92m'
		,'\x1b[0;93m'
		,'\x1b[0;94m'
		,'\x1b[0;95m'
		,'\x1b[0;96m']




	def DrawScreen(this):
		hr1,hr2 = this.hour
		mn1,mn2 = this.min

		if this.rainbow:
			offset = rint(0,4)
			color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11 = this.colors[offset:11+offset]
		else:
			color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11 = ["","","","","","","","","","",""]


		n11,n12,n13,n14,n15,n16,n17,n18,n19,n110,n111 = this.numbers[hr1].split('\n')[1:-1]
		n21,n22,n23,n24,n25,n26,n27,n28,n29,n210,n211 = this.numbers[hr2].split('\n')[1:-1]
		n31,n32,n33,n34,n35,n36,n37,n38,n39,n310,n311 = this.numbers[mn1].split('\n')[1:-1]
		n41,n42,n43,n44,n45,n46,n47,n48,n49,n410,n411 = this.numbers[mn2].split('\n')[1:-1]
		msg = f"""
{color1}{n11}  {n21}        {n31}  {n41}{color2}
{n12}  {n22}        {n32}  {n42}{color3}
{n13}  {n23}        {n33}  {n43}{color4}
{n14}  {n24}        {n34}  {n44}{color5}
{n15}  {n25}  ██    {n35}  {n45}{color6}
{n16}  {n26}        {n36}  {n46}{color7}
{n17}  {n27}  ██    {n37}  {n47}{color8}
{n18}  {n28}        {n38}  {n48}{color9}
{n19}  {n29}        {n39}  {n49}{color10}
{n110}  {n210}        {n310}  {n410}{color11}
{n111}  {n211}        {n311}  {n411}
"""[1:-1]

		clear()
		# print the numbers
		print(msg)


		YearMonthDay = f"{this.time.day}-{this.time.month}-{this.time.year}"
		today = datetime.date(int(this.time.year),int(this.time.month),int(this.time.day))
		weekday = this.weekdays[today.weekday()]

		# print day-month-year and day of the week
		print(this.bdp.load(),end='')
		print(YearMonthDay.rjust(38),end=f"\n{weekday.rjust(37)}")


	def Main(this):
		this.DrawScreen()
		try:
			while True:
				if this.min != this.LastTime:
					this.DrawScreen()
					this.LastTime = this.min
				else:
					sleep(1.3)
		except KeyboardInterrupt:
			clear()
			return 0


#start
if __name__ == '__main__':
	argv.pop(0)
	argv = argv_assing(argv)

	if (debug:='--debug' in argv.keys()):
		start = tm()

	exit_code = Program(argv).Main()

	if debug:
		if not exit_code:print(f'{color["green"]}code successfully exited in',end='')
		else:print(f'{color["red"]}code exited with error {exit_code} in',end='')
		print(f' {round(tm()-start,5)} seconds{color["nc"]}')
	exit(exit_code)
