import sys
import math

data = open(sys.argv[-1],'r').read().split('\n')

a = []

for i in data:
    a.append(int(i))


data = a

of = []





for i in data:
    a = math.floor(i/3)-2
    b = 0
    c = a
    of.append(a)
    while True:
        b = math.floor(c/3)-2
        if b<=0:
            break
        of.append(b)
        c = b

print(sum(of))