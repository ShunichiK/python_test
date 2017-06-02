#!/usr/bin/env python
import re

print "Chromosome,Gene Count,Avg Size"

p = re.compile("(\w+)\s+FlyBase\s+gene\s+(\d+)\s+(\d+)")
'''
2L|2R|3L|3R|4|X|Y|mitochondrion_genome|rDNA
'''
d = {}
e = {}
g = {}
with open("dmel-all-r6.10.gtf", "r") as f:
		for l in f.readlines():
			if p.search(l):
				r = p.search(l)
				c = r.group(1)
				if not c.startswith('211')|c.startswith('Unmapped'):
					if c in d:
						d[c] += 1
					else:
						d[c] = 1
						e[c] = 0
					e[c] += int(r.group(3))-int(r.group(2))+1 
				
for i in e.keys():
	g[i] = e[i]/d[i]

for i in sorted(d):
	print "%s\t%d\t%d" % (i, d[i], g[i])	


