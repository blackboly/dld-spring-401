def findMax(a, k = 0):
    max = a[0][k]
    for i in range(len(a)):
        if a[i][k] > max:
            max = a[i][k]
    return max


x = 1
l = []
l.append(x)
n, q = map(int, input().split())
a = list(map(int, input().split()))
p = []
for i in range(q):
    d, c = map(int, input().split())
    p.append([d, c])
    
m = findMax(p)
for i in range(m):
    a = a
print(m)