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
        self.result = ''
        self.operator = ['+', '-', '*', '/', ]
        self.i = 0
       
    def printResult(self):
        self.process()
        print(self.result)
    
    def process(self):
        s = stack()
        
        while self.i != self.size:
            if self.str[self.i] == ')':
                while  not s.empty():
                    self.result += s.pop()
                return 
            elif self.str[self.i]  not in self.operator:
                if self.str[self.i] != '(':
                    self.result += self.str[self.i]
                else:
                    self.i +=1
                    self.process()
            else:
                if s.empty():
                    s.push(self.str[self.i])
                elif ((s.top() == '-' or s.top() == '+') and 
                        (self.str[self.i] == '*' or self.str[self.i] == '/')):
                    s.push(self.str[self.i])
                else:
                    while  not s.empty():
                        if ((s.top() == '-' or s.top() == '+') and 
                            (self.str[self.i] == '*' or self.str[self.i] == '/')):
                            break
                        self.result += s.pop()
                    s.push(self.str[self.i])
            self.i+=1
            
        while  not s.empty():
            self.result += s.pop()
            
s = input()           
solve = postOrder(s)
solve.printResult()