name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
box = dict()
for line in handle:
    if not line.startswith('From '): continue
    nl = line.split()
    lst.append(nl[1])
    box[nl[1]] = box.get(nl[1], 0) + 1

bign = None
for s,n in box.items():
    if bign is None or n > bign:
        bign = n
        bigs = s
        
print(bigs,bign)
