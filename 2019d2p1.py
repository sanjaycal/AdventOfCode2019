import sys
import math

data = [int(x) for x in open(sys.argv[-1],'r').read().split(',')]






def run(indata):
    head = 0
    data = indata.copy()
    while True:
        if data[head]==1:
            data[data[head+3]] = data[data[head+1]] + data[data[head+2]]
            head +=4
        elif data[head]==2:
            data[data[head+3]] = data[data[head+1]] * data[data[head+2]]
            head +=4
        elif data[head]==99:
            break
    return data


data[1] = 12
data[2] = 2

a = run(data)
print(a[0])
