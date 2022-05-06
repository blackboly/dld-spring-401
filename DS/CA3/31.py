def max_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A, largest)

def left(k):
    return 2 * k + 1

def right(i):
    return 2 * i + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,k)

import random
A = []
for j in range(1000000):
    A.append(random.randint(0, 10000000))
import time
t1 = time.time()
build_max_heap(A)
t2 = time.time()
print("time: ", t2-t1)