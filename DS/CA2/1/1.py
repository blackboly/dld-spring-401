class A:
    def __init__(self):
        self.n = int(input())
        self.r = 0
        self.d1 = {}
        self.count = 0
        self.s = ""
        self.p = ""
    def solve(self):
        for i in range(self.n):
            if self.process():
                self.r +=1
            else:
                print("No")
            break
        if self.n == self.r:
            print("Yes")

    def process(self):
        self.s = input()
        self.n = len(self.s)
        self.p = input()
        self.d1 = {i:[True, 0] for i in self.p} 
        #test
        self.isMatch()
        #main
        # if self.isMatch():
        #     if
        #         return True
        # else:
        #     return False
    
    def print(self):
        print(self.d1)
    
    def equal(self):
        r= 0
        for key in self.p:
            r+=self.d1[key][1]
        return self.n-r
    #///////////////////////////
    def strMatch(self):
        result = ""
        d2 = {}
        for elm in self.s:
            if elm in d2:
                result+=d2[elm]
            else:
                d2[elm] = self.d1[elm]
        return True
    
    
    def isMatch(self):
        if self.equal() == 0:
            
            return True
        for i in range(1,self.n+1):
            
            k = ''
            t = 0
            for k in self.d1:
                if self.d1[k][0]:
                    t = 1
                    break
            if t == 0:
                return False
            
            self.d1[k][1] += 1
            self.d1[k][0] = False 
            if self.equal() < 0:
                return False
            self.count +=1
            print(self.count)
            if self.isMatch():
                return True
            self.d1[k][0] = True
        return False
            
        

    
a = A()
a.process()
a.print()






