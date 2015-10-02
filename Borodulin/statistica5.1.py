from random import *
float2=open('float_data.txt','w')
for i in range(1000000):
    print('%.2f' %(100*random()), file=float2,end=' ')
float2.close()
