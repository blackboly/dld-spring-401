def merge(left, right):
    result = []
    x, y = 0, 0
    for k in range(0, len(left) + len(right)):
        if x == len(left): 
            result.append(right[y]) 
            y += 1
        elif y == len(right):
            result.append(left[x])
            x += 1
        elif right[y] > left[x]:
            result.append(right[y])
            y += 1
        else:
            result.append(left[x])
            x += 1
    return result
def mergesort(ar_list):
    length = len(ar_list)
    size = 1
    while size < length:
        size+=size 
        for pos in range(0, length, size):
            start = pos
            mid = pos + int(size / 2)
            end = pos + size
            left = ar_list[ start : mid ]
            right = ar_list[ mid : end ]
            ar_list[start:end] = merge(left, right)
    return ar_list

def add(l, x, e, s=0):
    mid = (s+e)//2
    

def add2(l, x):
    n = len(l)-1
    while n > 1:
        l[n] +=x
        n//=2
              
    


import random
A = []
n = 100000
for j in range(n):
    A.append(random.randint(0, 10*n))
import time
t1 = time.time()
mergesort(A)
t2 = time.time()
print("time: ", t2-t1)
while n >2:
    try:
        M = A[-1] + A[-2]
    except:
        print(n, len(A))
    add2(A, 5)
    add2(A, 5)
    add2(A, 5)
    add2(A, 5)
    add2(A, 5)
    n -= 1
t2 = time.time()
print("time: ", t2-t1)
# print(A)