#!/usr/bin/python2
import time
import webbrowser
import os

x='''
press 1: to check date and time
press 2: to create a file
press 3: to create a directry
press 4: to search on google
press 5: power off
press 6: logout your system
press 7: shutdown your os
press 8: to check internet connection in your pc
press 9: to login whats app on browser
press 10: to  check all connected ip in your network

'''

choice=raw_input()
if choice == '1':
	print "showing date and time"
	print time.ctime().split()[3]  
#time.ctime is a function whic show time and date 
#.split() is a function which convert string file in list and [3] define position
#first time date in string foerm after applied function convert in list 

elif choice=='2':
	path="/root/Desktop/"
	msg5=raw_input("file name")
	os.system('touch ' +path+msg5)
	msg6="file is created"
	print msg6

elif choice=='4':
	print "searching on google..."
	msg=raw_input("type for searching")
	webbrowser.open_new_tab('https://www.google.com/search?q='+msg)
#msg vali line jb use krte h jb apn ko kuch search krna h ex. code 9  me msg vali line ka use nii liya kuki vha apn ko direct kolna h

elif choice=='5':
	print "close all app in your os"
	msg1="bhai ab bas abhi band apna pc"
	print msg1
	time.sleep(3)
	msg2="bhai tu to gya  aaj"
	print msg2
	time.sleep(2)
	os.system('poweroff')
#time.sleep is a function who stop the program for some time


elif choice=='6':
	print "logout your system"
	time.sleep(2)
	msg4="ab bas band h"
	print msg4
	time.sleep(2)
	os.system("pkill -kill -u " + os.getlogin())
#for voice remove "print msg4" and place "os.system('echo '+msg4+' | festival --tts')"
#time.sleep() command is stop programe in time()
#time.sleep command is self choice apni  icha h bhai 


elif choice=='7':
	print "close all app in your os"
	msg1="ab bas band hai apna pc"
	os.system('echo '+msg1+'  | festival --tts')
	time.sleep(3)
	msg2="bhai ab kitna sunega"
	os.system('echo  '+msg2+'  | festival --tts')
	time.sleep(2)
	os.system('reboot')
#os.system function use because voice massege use      echo ke bad jo bhi likte h vo vahi print krta h 
# | festival --tts cammand h voice ka text to speech    isme print se msg kpo define nii krege because apn ne yha massege voice se btaYA H




elif choice=='9':
	print "opening whatsapp"
	webbrowser.open_new_tab('https://web.whatsapp.com/')
#code 4 me nzr dall le bhai
else:
	print "wrong statement "

