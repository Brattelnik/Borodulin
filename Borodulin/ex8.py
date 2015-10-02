__author__ = 'student'
A=[1,2,3,2,3,3]
max=0
for i in range (0,len(A)):
    if A.count(A[i])>max:
        max=A.count(A[i])
        n=A[i]
print(n)