from random import *
output = open('int_data.txt', 'w')
for i in range(0,999999):
    a=randint(0,100)
    a=str(a)+' '
    output.write(a)
output.close()
