#!/Users/user12/anaconda/bin/python

import re

pat = re.compile(r'<A HREF="#\w+">(.+|.\s\.+|\.+\s\.+\s\.+|)</A>')
paat = re.compile(r'Sequence downloads only')
print ""
try:
    while True:
		s = raw_input()
		result = pat.search(s)		
		if result != None:
			if result.group(1).startswith("<"):
				print result.group(1).replace('<em>X. tropicalis</em>','X. tropicalis')
			else:	
				print result.group(1)
		if paat.search(s):
			break	
except EOFError, e:
	pass			