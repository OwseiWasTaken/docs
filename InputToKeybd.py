#! /bin/python3.9
from pynput.keyboard import Key, Controller
from util import sleep
KeyBoard = Controller()

ToPress = """
InputToKeybd.py
"""

def PressKey(key):
	KeyBoard.press(key)
	sleep(0.01)
	KeyBoard.release(key)

sleep(0.5)
for i in ToPress[:-1]:
	if i == '\n':continue
	sleep(0.05)
	PressKey(i)


