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

elif choice=='2':
	path="/root/Desktop/"
	msg1=raw_input("file name")
	os.system('touch ' +path+msg1)
	msg2="file is created"
	print msg2


elif choice=='3':
	path="/root/Desktop/"
	msg8=raw_input("type name")
	os.system('touch ' +path+msg8)
	print "directry is created"	

elif choice=='4':
	print "searching on google..."
	msg3=raw_input("type for searching")
	webbrowser.open_new_tab('https://www.google.com/search?q='+msg3)

#open new tab beacause opening result in new tab


elif choice=='5':
	print "if you want to shut down your pc y/n"
	y='''
	press y: shut down
	'''
	choice1=raw_input()
	if choice1=='y':
		print "ok processing is going on your pc will be shut down after 15 minut...."
		time.sleep(900)
		os.system('poweroff')
	else:
		print "thanks"
#time.sleep is a function who stop the program for some time
#second time for ask permission to y/n another raw_input define with another variable

elif choice=='6':
	print "logout your system"
	time.sleep(2)
	msg4="now shut down"
	print msg4
	time.sleep(2)
	os.system("pkill -kill -u " + os.getlogin())

elif choice=='7':
	print "close all app in your os"
	msg5="shut down app"
	os.system('echo '+msg5+'  | festival --tts')
	time.sleep(3)
	msg7="proseser is going on"
	os.system('echo  '+msg7+'  | festival --tts')
	time.sleep(2)
	os.system('reboot')
# festival --tts is cammand who convert text to speech
# for voice output ('echo '+msg+' | festival --tts')



elif choice=='9':
	print "opening whatsapp"
	webbrowser.open_new_tab('https://web.whatsapp.com/')

else:
	print "wrong statement "

