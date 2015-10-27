__author__ = 'IVAN BORODULIN'
from decimal import Context,Decimal

def PROCENTY(S):

    return  Decimal(x)/100

S=float(input())
x=float(input())
y=int(input())
S=Decimal(S).quantize(Decimal('0.01'))

for i in range(12*y):
    S += PROCENTY(S)
    print(S)


