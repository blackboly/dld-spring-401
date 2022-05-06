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

    def removeMin2(self):
        min1 = self.q[0]
        if self.n == 2:
            return min1 + self.q[1]
        smallest = 1 if self.q[1] < self.q[2] else 2
        min2 = self.q[smallest]
        if self.n == 3:
            biggest = 2 if smallest ==1 else 1
            self.n -=1
            if self.q[biggest] < (min1 +min2):
                self.q[0] = self.q[biggest]
                self.q[1] = min1 + min2
            else:
                self.q[0] = min1 + min2
                self.q[1] = self.q[biggest]
            return min1 + min2
        self.n -=1
        self.q[0] = self.q[self.n]
        self.q[smallest] = min1 + min2
        self.maxHeapify(smallest)
        self.maxHeapify(0)
        return min1 + min2

n = int(input())
l = list(map(int, input().split()))
p = heap(l, n)
p.buildMaxHeap()

s = 0
for _ in range(n-1):
    t = p.removeMin2()
    s += t
    
print(s)
