#!/Users/user12/anaconda/bin/python

import sys

if len(sys.argv) <= 2:
	print >> sys.stderr, "Usage: linenumber.py<input file> <output file>"
	sys.exit(1)

input_file_name = sys.argv[1]
output_file_name= sys.argv[2]

line_count = 0
with open(input_file_name, "r") as fin:
	with open(output_file_name, "w") as fout:
		for l in fin.readlines():
			line_count += 1
			print >>fout, ("%4d:" % line_count), l.strip()
