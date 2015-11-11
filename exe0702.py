fname = raw_input("Enter file name: ")
if len(fname)==0:
    fname="mbox-short.txt"
fh = open(fname)
count=0.0
sum=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
		count=count+1
		temp=float(line[line.find(":")+1:])
		sum=sum+temp
print "Average spam confidence: %.12f"%(sum/count)
