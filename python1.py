#!/usr/bin/python3
import os
import sys
import webbrowser
var=int(input("Press1:Date, Press2:Calender, Press3:Shutdown, Press4:For IP, Press5:ALL IP, Press6:Google Search"))
if(var==1):
	os.system('date')
elif(var==2):
	os.system('calender')
elif(var==3):
	os.system('shutdown -H -T -5')
elif(var==4):
	os.system('hostname -I')
elif(var==5):
	os.system('ifconfig')
elif(var==6):
	wb=input("Enter Keywords")
	webbrowser.open_new_tab('https://www.google.com/search?q={}.format(wb)')
else:
	print("Wrong Input")
