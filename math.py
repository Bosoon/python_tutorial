#!/usr/bin/env python

sum=0
count=100
value=0.6
time=0.1
temp=0

while(count>0):
    temp=value*count
    value=value*time
    count=count-1
    print temp
    sum=sum+temp

print sum
