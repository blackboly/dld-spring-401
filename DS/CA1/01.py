# def processInput(x):
#     out = []
#     for i in x:
#         count = 0
#         for j in x:
#             if i == j:
#                 count+=1
#         out.append(count)
#     return out

def processInput(a):
    elements_count = {}
    for element in a:
        if element in elements_count:
            elements_count[element] += 1
        else:
            elements_count[element] = 1
    out = []
    for element in a:
        out.append(elements_count[element])
    return out

n, q = map(int, input().split())
a = list(map(int, input().split()))  
p = [[0,0]for i in range(q)]
for i in range(q):
    p[i][0], p[i][1] = map(int, input().split())

        
        
