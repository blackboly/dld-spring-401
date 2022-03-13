def findMax(a, k = 0):
    max = a[0][k]
    for i in range(len(a)):
        if a[i][k] > max:
            max = a[i][k]
    return max

def g(a, out):
    elements_count = {}
    for element in a:
        if element in elements_count:
            elements_count[element] += 1
        else:
            elements_count[element] = 1
    for element in a:
        out.append(elements_count[element])

n, q = map(int, input().split())
a = list(map(int, input().split()))
C = []
D = []
for i in range(q):
    c ,d = (map(int, input().split()))
    C.append(c)
    D.append(d)

ma = max(C)
l = [[]for i in range(ma+1)]
l[0] = a
for i in range(ma):
    g(l[i], l[i+1])
    
for i in range(len(C)):
    print(l[C[i]][D[i]-1])