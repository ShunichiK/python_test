#!/Users/user12/anaconda/bin/python

a = 100000
c=0
while 0 < a:
    b = a
    while 0 < b:
        c += 1 
        b = b - 1
    a = a - 1
print c

with open('test3.txt', "w") as f:
	print >>f, "Hello, babeeeeeee"
	print >>f, "ssssssss"

