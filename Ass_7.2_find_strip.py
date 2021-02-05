# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x += 1
    dd = line.find(':')
    nl = line[dd+1:].strip()
    nl2 = float(nl)
    y += nl2
    
z = y/x
print("Average spam confidence:", z)