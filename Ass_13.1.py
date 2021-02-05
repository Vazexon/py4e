import re
name = input('Enter file name: ')
if len(name) < 1: name = 'New Text Document.txt'
handle = open(name)
#nh = handle.read()
#num = re.findall('\d+', str(nh))
#s = 0
#for x in num:
#    x = int(x)
    #s += x
#print(s)

print( sum( [ int(x) for x in re.findall('[0-9]+', handle.read()) ] ) )
