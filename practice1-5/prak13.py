a=list(map(int,input().split()))
b=[a[i] for i in range(len(a)-1) if (a[i]!=2 or a[i+1]==2)]+[a[-1]]
print(int(sum(b)/len(b)))
