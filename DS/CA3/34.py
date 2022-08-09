class bst:
    def __init__(self, x):
        self.x = x
        self.right = None
        self.left = None

def add(root, x):
    n = bst(x)
    prep = None
    p = root
    while p:
        prep = p
        if x < p.x:
            p = p.left
        else:
            p = p.right 
            
    if prep is None:
        root = n
    else:
        if x < prep.x:
            prep.left = n
        else:
            prep.right = n 
             
def insert(root, x):
    if root is None:
        return bst(x)
    
    if x < root.x:        
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
                
    return root            
          
def delMin(root, s):
    
    if root.left is None:
        s[0] += root.x
        return root.right
    q = root
    while q.left:
        p = q
        q = q.left
    if q.right is None:
        p.left = None
    p.left = q.right
    s[0] += q.x

    return root

        
        
import random
import time
# n = int(input())
n = 10000
l = []   
for _ in range(n):
    l.append(random.randint(1, 100000000))
# l = list(map(int, input().split()))
t1 = time.time()
 

q = bst(l[0])
for i in range(1, len(l)):
    add(q, l[i])

s = 0

for _ in range(n-1): 
    m = [0] 
    
    q = delMin(q, m)
    q = delMin(q, m)
    add(q, m[0])
    s +=m[0]
 
    
print(s)
t2 = time.time()
print(t2- t1)


        