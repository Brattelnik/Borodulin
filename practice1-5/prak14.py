n=int(input())
a=[tuple(map(int,input().split())) for i in range(n)]
t=int(input())
c=0
for i in range(n):
    if t in range(a[i][0], a[i][1]+1): c+=1
print(c)
