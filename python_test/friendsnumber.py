#!/usr/bin/env python


d={}
while True:

	a=raw_input()
	b=raw_input()

	if a == 'END' and b == 'END':
		break
	if a in d:
		d[a] += 1
	else:
		d[a] = 1 
	if b in d:
		d[b] += 1
	else:
		d[b] = 1
	

name= max(d.items(), key=lambda x:x[1])[0]
number= max(d[x] for x in d)

print name,number