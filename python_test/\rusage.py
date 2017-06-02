#!/usr/bin/env python

import time
import sys

for i in range(100):
	print "%3d%%\r" % i,
	sys.stdout.flush()
	time.sleep(0.1)

print "100%"
