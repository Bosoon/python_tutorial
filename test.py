#!/usr/bin/env python

time=0.1
count=100
sum=0.0
temp=9.0

while(count>0):
	temp=temp*time
	sum=sum+temp*count
	print temp
	count=count-1

print sum
