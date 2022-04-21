import numpy as np 

def compareTriplets(a,b):
    r = np.array([0,0], dtype=np.int32)
    for i in range(len(b)):
        if a[i]>b[i]: r[0]+=1
        elif b[i]>a[i]: r[1]+=1
    return r

a = list(map(float, input().split()))
b = list(map(float, input().split()))

print(compareTriplets(a,b))





