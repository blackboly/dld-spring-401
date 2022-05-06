class bst:
    def __init__(self, x):
        self.x = x
        self.right = None
        self.left = None
        
def insert(root, x):
    if root is None:
        return bst(x)
    
    if x < root.x:        
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)
                
    return root 
           
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


a= bst(5)
s = [0]
add(a, 6)
add(a, 7)
add(a, 3)
add(a, 2)
add(a, 4)
add(a, 6.5)
print(a.x, a.left.x)
a = delMin(a, s)
print(s)
a = delMin(a, s)
print(s)
print(a.x, a.left.x)
# print(a.right.right.left.x)