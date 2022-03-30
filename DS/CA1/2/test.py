import time
l = [i%100 for i in range(1000000)]
def uniq(l):
    o = []
    for el in l:
        if el not in o:
            o.append(el)
    o.pop(0)
    return o



def uniq2(a):
    o = []
    for el in l:
        if el not in o:
            o.append(el)
    o.pop(0)
    return o      
            
t1 = time.time()
o1 = uniq(l)
t2 = time.time()
print("time 1: ",t2-t1)
t1 = time.time()
o3 = uniq2(l)
t2 = time.time()
print("time 2: ",t2-t1)
t1 = time.time()
o2 = set(l)
t2 = time.time()
print("time 3: ",t2-t1)