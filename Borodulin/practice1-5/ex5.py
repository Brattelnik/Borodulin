__author__ = 'student'
A=[1,2,3,4,5]
for i in range(0,len(A)//2*2,2):
    A[i],A[i+1]=A[i+1],A[i]
print(A)