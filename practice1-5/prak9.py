A = input().split()
B=[0]*len(A)*2
B[1::2]=A[::-1]
B[::2]=A
A=B[:len(A)]
print(' '.join(A))
input()

