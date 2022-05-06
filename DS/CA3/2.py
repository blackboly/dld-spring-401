class bst:
    def __init__(self, x, r):
        self.x = x
        self.right = None
        self.left = None
        self.r = r
        self.l = 0
        
    def insert(self, x):
        self.add(x, 0)
        
    def add(self, x, r):
        
        if self is None or self.x is None:
            self.__init__(x, r)
            
        elif x < self.x:
            self.l +=1
            if self.left is None :
                self.left = bst(x, r)
            else:
                self.left.add(x, r)
            
        else:
            if self.right is None:
                self.right = bst(x, 1)
            else:
                self.right.add(x, 1)
        
        
    def fuck(self, y, s=0, r=1):
        if y < self.x:
            if self.left is None:
                return s
            else:
                return self.left.fuck(y, s, r)
        else:
            if self.right is None:
                s = s + self.r + self.l + r
                return s
            else:
                s += (self.r + self.l + r)
                r = 0
                return self.right.fuck(y, s, r)
        
a = bst(None, None)
a.insert(10)
a.insert(15)
a.insert(5)
a.insert(4)
a.insert(6)
a.insert(8)
a.insert(7)
a.insert(16)
a.insert(12)
print(a.fuck(14.5))
# print(a.left.right.r, a.left.right.l)

        