#!/usr/bin/env python

import csv

data=[]
data2=[]
data3=[]
data4=[]
output_data=[]

a = int(raw_input())
b = int(raw_input())

reader= csv.reader(raw_input() for i in range(3))
for row in reader:
	data.append(row)
'''
data= [raw_input() for i in range(3)]

data2= data[0].split(",")
data3= data[1].split(",")
data4= data[2].split(",")
'''
data2= data[0]
data3= data[1]
data4= data[2]
data2[a-1],data2[b-1]= data2[b-1],data2[a-1]
data3[a-1],data3[b-1]= data3[b-1],data3[a-1]
data4[a-1],data4[b-1]= data4[b-1],data4[a-1]
output_data=[data2,data3,data4]


with open("name.csv","w") as fout:
	writer = csv.writer(fout)
	writer.writerows(output_data)

'''
output_data= "%s,%s,%s\n%s,%s,%s\n%s,%s,%s" % (data2[0],data2[1],data2[2],data3[0],data3[1],data3[2],data4[0],data4[1],data4[2])
print output_data
'''



'''
ans 
['Family_Name,First_Name,ID', 'Yamada,Taro,018288193', 'Yamada,Hanako,342449259']
'''

'''
import json
List = ['A', 'B']
print json.dumps(List)
'''

'''
str = "Taro,Jiro,Saburo,Hanako"
print str.split(",") 
'''

'''
print data
for i in range(3):
	data2.append((data[i]))
print data2

data2[0][a],data2[0][b]=data2[0][b],data2[0][a]
data2[1][a],data2[1][b]=data2[1][b],data2[1][a]
data2[2][a],data2[2][b]=data2[2][b],data2[2][a]
'''


'''
data2.append(data[0])
print json.dumps(data2)

data3=[]
data4=[]
data3.append(data[1])
data4.append(data[2])
print data2
print json.dumps(data2).split(",")
data2[a],data2[b]=data2[b],data2[a]
data3[a],data3[b]=data3[b],data3[a]
data4[a],data4[b]=data4[b],data4[a]


with open(name.csv,"w") as fout:
	writer = csv.writer(fout, lineterminator='\r')
	writer.writerow(data2,data3,data4)
'''