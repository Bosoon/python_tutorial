name = raw_input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
temp=list()
lst=list()
dic=dict()

for line in handle:
    line=line.strip()
    if line.startswith('From '):
        temp=line.split()
        lst.append(temp[1])

for address in lst:
    dic[address]=dic.get(address,0)+1

manyAddress=None
manyCount=None

for address,count in dic.items():
    if manyCount is None or count>manyCount:
        manyAddress=address
        manyCount=count

print manyAddress,manyCount
