n=int(input())
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
p=int(input())
max=0
for i in range(0,n-p+1):
    a=sum(A[i:p])
    if a>max:
        max=a
print(max)       
input()
    
