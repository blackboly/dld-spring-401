def processInput(x):
    out = []
    for i in x:
        count = 0
        for j in x:
            if x[i] == x[j]:
                ++count
        out.append(count)
        count = 0
    return out

def inputHandler(x):
    c, d = map(int, input().split())
    out = x
    for i in range(c):
        x = processInput(x)
    print(x[d])

      
n, q = map(int, input().split())
a = list(map(int, input().split()))

for i in range(q):
    inputHandler(a)