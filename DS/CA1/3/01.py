s = input()
n = len(s)
out1 = 0
for i in range(n//2):
    if s[i] != s[n-(i+1)]:
        out1+=1
out2 = (2**out1)%(10**9 + 7)
print(out1,out2)


