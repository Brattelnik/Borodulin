k=int(input())
n=int(input())
A=[0]*(n+2)
for i in range(0,n+2):
    A[i]=1
    if i>k:
        A[i]=sum(A[i-k:i])
print(A[n+1])
