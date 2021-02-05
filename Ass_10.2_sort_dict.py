name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
l = list()
d = dict()
for line in handle:
    if not line.startswith('From '): continue
    lst = line.split()
    nl = lst[5].split(':')
    l.append(nl[0])
    
for x in l:
    d[x] = d.get(x, 0) + 1

for x, y in sorted(d.items()):
    print(x, y)
