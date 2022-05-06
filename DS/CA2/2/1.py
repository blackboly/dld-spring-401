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

       
class JKh:
    def __init__(self):
        self.n = int(input())
        self.l = list(map(int,input().split()))
        self.Stacks = []
        for i in range(self.n):
            self.Stacks.append(stack())
        self.sum = [0 for i in range(self.n)]
        self.result = 0
        
    def createStack(self, elm, i=0):
        if i == len(self.Stacks):
            return
        self.sum[i]+=elm 
        if self.Stacks[i].empty():
            self.Stacks[i].push(elm)
        else:
            newElm = max(self.Stacks[i].top(), elm)
            self.Stacks[i].push(elm)
            self.createStack(newElm,i+1)
    
    def Sum(self):
        for i in range(len(self.sum)):
            c = i+1
            self.result+= c*self.sum[i]
            
    def printSum(self):
        print(*self.sum)
        
    def printStack(self):
        for i in range(len(self.Stacks)):
            self.Stacks[i].print()
        
    def answer(self):
        self.Sum()
        print((self.result)%(10**9 + 7))
        
    def work(self):
        for i in range(self.n):
            self.createStack(self.l[i])
            
            
solve = JKh()
solve.work()
solve.answer()

    