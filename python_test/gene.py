import sys, re

if len(sys.argv) <= 1:
	print >> sys.stderr, "Usage: acgt_count.py <input multi-FASTA>"
	sys.exit(1)

input_file_name = sys.argv[1]

def show_gene_composition(name, d):
	if name == None: return
	
	num_a = d['A'] if 'A' in d else 0
	num_c = d['C'] if 'C' in d else 0
	num_g = d['G'] if 'G' in d else 0
	num_t = d['T'] if 'T' in d else 0
	num_cg = num_c + num_g
	num_at = num_a + num_t
	num_all = num_cg + num_at
	print name, "\t\tGC %4.1f%%\t%d" % (int(num_cg * 100.0 / num_all), num_all)



	#print name, ":"
	#for k, v in d.items():
	#	print "\t" + k + ": " + str(v)
print 'Gene name\tGC content\tLength'

d= {}
c= raw_input()
pat = re.compile(c)
current_gene_name = None
try:
	with open(input_file_name, "r") as f:

		for l in f.readlines():
			l = l.strip()
			if len(l) == 0:
				continue
			if l[0] == '>':
				show_gene_composition(current_gene_name, d)
				current_gene_name = l[1:]
				d={}
				continue
			len(re.findall(c, l))
	show_gene_composition(current_gene_name, d)
					
except IOError, e:
	print "I/O error: ", e
	print "Check the input file ('%s')" % input_file_name	