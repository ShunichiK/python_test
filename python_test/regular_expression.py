#!/usr/bin/env python

import re


p = re.compile("\s(.+?)\sSGDID")
q = re.compile("(Chr\s.*?)\sfrom")

with open("test4.txt", "r") as f:
	for l in f.readlines():
		if p.search(l):
			r = p.search(l)
			if q.search(l):
				s = q.search(l)
				print "%s%s%s" %(r.group(1).strip(),",",s.group(1))
			else:
				s = "plasmid"	
				print "%s%s%s" %(r.group(1).strip(),",",s)
		else:
			continue
		

	