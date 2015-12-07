n=int(input())
a=[[1]]
for i in range(n):
    a+=[[([0]+a[-1])[j]+(a[-1]+[0])[j] for j in range(len(a[-1])+1)]]
print('\n'.join([' '.join(list(map(str, i))) for i in a]))
