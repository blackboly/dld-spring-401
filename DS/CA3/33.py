class heap:
    
    def __init__(self, q, n):
        self.q = q
        self.n = n
    
    def maxHeapify(self, k):
        l = self.left(k)
        r = self.right(k)
        if l < self.n and self.q[l] < self.q[k]:
                smallest = l
        else:
            smallest = k
        if r < self.n and self.q[r] < self.q[smallest]:
                smallest = r
        if smallest != k:
            self.q[k], self.q[smallest] = self.q[smallest], self.q[k]
            self.maxHeapify(smallest)

    def left(self, k):
        return 2 * k + 1

    def right(self, k):
        return 2 * k + 2

    def parent(self, k):
        return (k-1)//2
        
    def buildMaxHeap(self):
        n = int((self.n//2)-1)
        for k in range(n, -1, -1):
            self.maxHeapify(k)
    
    def __str__(self):
        return str(self.q) 
    
    def add(self, elm):  
        self.q[self.n] = elm
        self.n +=1
        i = self.n-1
        while i>0 and self.q[i] < self.q[self.parent(i)]:
            self.q[i] ,self.q[self.parent(i)] =  self.q[self.parent(i)] ,self.q[i]
            i = self.parent(i)
    
    def removeMin(self):
        min1 = self.q[0]
        if self.n == 2:
            return min1 + self.q[1]
        
        smallest = 1 if self.q[1] < self.q[2] else 2
        min2 = self.q[smallest]
        self.n -=1
        self.q[0] = self.q[self.n]
        self.q[smallest] = min1 + min2
        self.maxHeapify(smallest)
        self.maxHeapify(0)
        return min1 + min2


import random
import time
# n = int(input())
n = 100000
l = []
for _ in range(100000):
    l.append(random.randint(1, 100000000))
# l = list(map(int, input().split()))
 
p = heap(l, n)
t1 = time.time()
p.buildMaxHeap()
t2 = time.time()
print(t2- t1)
s = 0
for _ in range(n-1):
    t = p.removeMin()
    # p.add(t)
    s += t
    
print(s)