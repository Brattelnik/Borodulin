__author__ = 'Ivan'
import math
def A(x):
    z=None
    if x==1 or 1/(1-x)+21/8==0:
        z='Neopredelen'
    else:
        z=(x**7+2*x**3-(3/(1+x**2)))/((1/(1-x)) +21/8)
    return z
def B(x):
    y=None
    if math.sin(x/(x**2+2))+math.exp(math.log1p(x)+1)==0 or x==0:
        y='Neopredelen'
    else:
         y=(1/(math.sin(x/(x**2+2))+math.exp(math.log1p(x)+1)))-1
    return y

for i in range(1,11):
    print(i,A(i),B(i))



