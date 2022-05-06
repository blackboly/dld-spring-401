class stack:
    def __init__(self):
        self.s = []
        
    def empty(self):
        return len(self.s) == 0
    
    def top(self):
        if self.empty():
            return
        return self.s[-1]
    
    def push(self, elm):
        self.s.append(elm)
        
    def pop(self):
        if self.empty():
            return
        out = self.s[-1]
        self.s.pop()
        return out
        
    def print(self):
        print(*self.s)
        
    def size(self):
        return len(self.s)


class postOrder:
    def __init__(self, str):
        self.str = str
        self.size = len(str)
        self.result = ""
        self.operator = ['+', '-', '*', '/', ]
        
       
    def printResult(self):
        self.process()
        print(self.resutl)
    
    def process(self, i=0):
        s = stack()
        while i != self.size:
            if self.str[i] == ')':
                while  not s.empty():
                    self.result =+ s.pop()
                return 
            if self.str[i]  not in self.operator:
                if self.str[i] != '(':
                    self.result += self.str[i]
                else:
                    self.process(i+1)
            else:
                if s.empty():
                    s.push(self.str[i])
                elif (s.top() == ('-' or '+') and self.str[i] == ('/' or '*')):
                    s.push(self.str[i])
                else:
                    while  not s.empty():
                        self.result =+ s.pop()
                    s.push(self.str[i])
            i+=1
            
        while  not s.empty():
            self.result =+ s.pop()
            
# s = input()           
# solve = postOrder(s)
# solve.printResult()

s = stack()
s.push('b')
s.push('c')
result = ''
result += s.pop()
print(result)