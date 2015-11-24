fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    abc=line.split()
    for item in abc:
        if item in lst:
            continue
        lst.append(item)

result=lst.sort()
print lst
