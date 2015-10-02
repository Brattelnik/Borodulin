С=list(map(int,input().split()))
t=int(input())
while t>=1:
    С.insert(((len(С)-1)-С[len(С)-1]),С[len(С)-1])
    С.pop()
    t-=1
print(С)
