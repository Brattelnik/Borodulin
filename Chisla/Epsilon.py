__author__ = 'IvanBORODULIN'
n=1
while n!=0:
    if 2**(-n-1)+1==1 and 2**(-n)!=0:
        k=n
        n=0
    else:
        n=n+1
print("e=",2**(-k))
