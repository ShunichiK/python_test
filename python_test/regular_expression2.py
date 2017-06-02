#!/usr/bin/env python

import re


p = re.compile("added\s(\d+)\s")


while True:
	l=raw_input()
	if p.search(l):
		r = p.search(l)
		print r.group(1).strip()
	else:
		continue