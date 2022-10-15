import subprocess

#####-----This part of code is for aesthetics-----#####

import time
import threading
import random
import os

#this just maximises cmd
'''
import ctypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
user32 = ctypes.WinDLL('user32', use_last_error=True)
hWnd = kernel32.GetConsoleWindow()
SW_MAXIMIZE = 3 # 2 is minimise
user32.ShowWindow(hWnd, SW_MAXIMIZE)
'''

#to fullscreen cmd
from pynput.keyboard import Key, Controller

keyboard = Controller()
keyboard.press(Key.f11)

def hacking_animation(start='',end=''):
	print('\nStarting Hacking Animation...\n')
	print(start)

	duration = 5 #seconds
	num_lines = 50
	max_length = 100 #max chars per line
	dt = duration/num_lines #seconds

	chars = "qwertyuiopasdfghjklzxcvbnm1234567890      [];,.?!@#$%^&*()_+-=~`"

	char_line = lambda : ''.join( chars[random.randint(0,len(chars)-1)] for i in range(random.randint(0,max_length)) )

	for i in range(num_lines):
		print(char_line())
		time.sleep(dt)

	print(end)

t1 = threading.Thread(target = hacking_animation, kwargs={'start':'Hacking Yo Passwords...\n'})
t1.daemon = True
t1.start()

#####-----Actual Code-----#####

wifis_output = subprocess.check_output(('netsh','wlan','show','profile')).decode('utf-8')
wifis = [line.split(':')[1].strip() for line in wifis_output.split('\n') if 'All User Profile' in line ]

passwords = []
for wifi in wifis:
	try:
		pass_output = subprocess.check_output(('netsh','wlan','show','profile',wifi,'key=clear')).decode('utf-8')
		if 'Key Content' in pass_output:
			for line in pass_output.split('\n'):
				if 'Key Content' in line:
					passwords.append(line.split(':')[1].rstrip('\r').lstrip(' '))
		else:
			passwords.append(None)
	except (IndexError,subprocess.CalledProcessError) as e:
		print(e)
		passwords.append(None)

t1.join()
print('\n***********************\n')
print('wifi passwords found on the system...')
print('wifi : password')
for i,j in zip(wifis,passwords):
	print(f'{i} : {j}')
print('\n***********************')
input()
