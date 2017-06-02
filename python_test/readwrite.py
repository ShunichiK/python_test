

line_count = 0
keyword_count = 0

x = raw_input()
keyword = raw_input()
y = raw_input()

try:
	with open(x,"r") as fin:
		with open(y,"w") as fout:
			for l in fin.readlines():
				line_count += 1
				if keyword in l:
					keyword_count += 1
					print >>fout, ("%s%d%s%d%s%s" %('line ',line_count,', hit #',keyword_count,': ',l.strip()))

except:
	print "ERROR"