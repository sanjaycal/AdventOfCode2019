import sys
import math

data = open(sys.argv[-1],'r').read().split('\n')

a = []

for i in data:
    a.append(int(i))


data = a

of = []

for i in data:
    of.append(math.floor(i/3)-2)

print(sum(of))