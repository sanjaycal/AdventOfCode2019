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



for n in range(100):
    for v in range(100):
        data[1] = n
        data[2] = v
        a = run(data)
        if(a[0]==19690720):
            print(100*n+v)
