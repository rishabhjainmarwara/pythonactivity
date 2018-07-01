#!/usr/bin/python
import os
import sys
#printing number of argument
#print sys.argv

# no of argument givin by user
noarg=len(sys.argv)


#  only working in single argument
arg_name=sys.argv[1] 
#showing help option to user

if noarg== 1:
	print "plz type any name after command"
	print "like pytouch  example,txt"
else:
	#checking current working directry name
	current_dir=os.getcwd()
#  listing all the content to working directory
	content_dir=os.listdir(current_dir)
	#  assigining content to for loop
	for i in content_dir:
		if arg_name in i:
			print  arg_name+"already exits"
		else:
			f=open(arg_name,"w")
			f.close()


