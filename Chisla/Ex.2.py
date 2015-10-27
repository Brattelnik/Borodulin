__author__ = 'IVANBORODULIN'
n=int(input())
A=[0]*(n+2)
A[0]=4.0000000000
A[1]=4.2500000000
for i in range(2,n+1):
    A[i]=108-(815-1500/A[i-2])/A[i-1]
print(A[n])