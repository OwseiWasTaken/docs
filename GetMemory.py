#! /usr/bin/python3.9
#imports
from os import system as ss
from struct import pack, unpack
from fcntl import ioctl
from termios import TIOCGWINSZ

x, y, *_ = unpack('HHHH',ioctl(0, TIOCGWINSZ,pack('HHHH', 0, 0, 0, 0)))
del _


ss("free -m | grep Mem | awk '{print ($3,$2,$3/$2)}' > /tmp/GetMem")
# make file w/ Mem values (tmp)

with open('/tmp/GetMem','r') as file:
	data = file.readlines()[0].split()
# read and store file's contents in /data/
# no need to delete file, it's small and in /tmp

pc = str(round(float(data[2])*100,2))
if len(pc) < 5:pc+='0'
# get info from data list (tmp file data)

color = ("\033[0;32m" if float(pc) <= 45 else "\033[0;31m")
# set msg color based of Mem %

print(f"><> | {color}Mem: {data[0]}M of {data[1]}M {pc}%\033[0m")
# print stuff
