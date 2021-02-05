import re
name = input('Enter file name: ')
if len(name) < 1: name = 'regex_sum_387340.txt'
handle = open(name)
nh = handle.read()
num = re.findall('[0-9]+', nh)
s = 0
for x in num:
    x = int(x)
    s += x
print(s)
