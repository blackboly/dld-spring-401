
n, q = map(int, input().split())
a = list(map(int, input().split())) 

elements_count = {}
for element in a:
   if element in elements_count:
      elements_count[element] += 1
   else:
      elements_count[element] = 1
out = []
for element in a:
    out.append(elements_count)[element]
