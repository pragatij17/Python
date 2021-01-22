#!/usr/bin/python3
import os
import sys
import webbrowser

n=1
while(n!=0):
	var=int(input(" Press 1 : Date \n Press 2 : Calendar \n Press 3 : Shutdown \n Press 4 : For IP \n Press 5 : ALL IP\n Press 6 : Google Search \n Press 0 : Exit\n"))

	if(var==1):
		os.system('date')
	elif(var==2):
		os.system('cal')
	elif(var==3):
		os.system('shutdown -H 05')
	elif(var==4):
		os.system('hostname -I')
	elif(var==5):
		os.system('ifconfig')
	elif(var==6):
		wb=input("Enter Keywords")
		webbrowser.open_new_tab('https://www.google.com/search?q='+wb)
	elif(var==0):
		n=0	
	else:
		print("Wrong Input")
