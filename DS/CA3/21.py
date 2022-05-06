class bst:
    def __init__(self, x, r):
        self.x = x
        self.right = None
        self.left = None
        self.r = r
        self.l = 0
                
    def add(self, x, r=0):
        
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
        
        
    def bigger(self, y, s=0, r=1):
        if self.x is None:
            return s
        if y < self.x:
            if self.left is None:
                return s
            else:
                return self.left.bigger(y, s, r)
        else:
            if self.right is None:
                s = s + self.r + self.l + r
                return s
            else:
                s += (self.r + self.l + r)
                r = 0
                return self.right.bigger(y, s, r)
            
            
            
n = int(input())
a = bst(None, None)

for i in range(n):
    k, m = map(int, input().split())
    if k == 1:
        a.add(m)
    if k == 2:
        print(a.bigger(m))  


        