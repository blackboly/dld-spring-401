from math import ceil

def generate(i = 0):
    if i == len(a):
        return True
    for l in a[i]:
        if l in elm:
            if elm[l] == ceil(n/2):
                continue
            else:
                result.append(l)
                elm[l]+=1
        else:
            result.append(l)
            elm[l] = 1;      
        if generate(i+1):
            return True
        elm[l]-=1
        result.pop()
    return False


def uniq():
    row.pop(0)
    for el in row:
        if el not in o:
            o.append(el)
  
n = int(input())
a = []
elm = {}

for i in range(n):
    row = list(input().split())
    o = []
    uniq()
    a.append(o)
 
 


result = []
single = 0

for v in a:
    if len(v)==1:
        single+=1
if single > ceil(n/2):
    print("NO")
else:
    if generate():
        print("YES")
        print(*result)
    else:
        print("NO")
