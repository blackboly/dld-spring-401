class stack:
    def __init__(self):
        self.s = []
        
    def empty(self):
        return len(self.s) == 0
    
    def top(self):
        return self.s[len(self.s)-1]
    
    def push(self, elm):
        self.s.append(elm)
        
    def pop(self):
        out = self.s[len(self.s)-1]
        self.s.pop()
        return out
        
    def print(self):
        print(*self.s)

l = []
for i in range(5):
    l.append(stack())
    
l[0].push(1)
for i in range(5):
    l[i].print()
