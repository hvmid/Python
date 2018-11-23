import os
import time

def turnOFF():
	os.system("blueutil -p 0")

current_time=(time.time())

while True:		
	if(((int)(current_time)%5)==0):
		turnOFF()
	current_time=(time.time())

