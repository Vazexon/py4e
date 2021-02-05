fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.strip().split()
    for x in line:
        if x not in lst:
            lst.append(x)
lst.sort()
print(lst)
