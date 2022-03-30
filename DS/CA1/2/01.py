from math import ceil

def generate(result, a, i = 0, elm = {}):
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
        if generate(result, a, i+1, elm):
            return True
        elm[l]-=1
        result.pop()
    return False


def uniq(l):
    o = []
    for el in l:
        if el not in o:
            o.append(el)
    o.pop(0)
    return o
  
n = int(input())
L = []
for i in range(n):
    a = list(input().split())
    L.append(uniq(a))
 
 


result = []
single = 0

for v in L:
    if len(v)==1:
        single+=1
if single > ceil(n/2):
    print("NO")
else:
    if generate(result, L):
        print("YES")
        print(*result)
    else:
        print("NO")
