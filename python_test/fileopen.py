#!usr/bin/env python

a = 0
x= raw_input()
try:
	with open(x,'r') as f:
		for l in f.readlines():
			a += 1
			print "%d%s%s" % (a,': ',l),


except:
	print "ERROR"