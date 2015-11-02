__author__ = 'Borodulin'
from decimal import Decimal,localcontext,Context
import numpy as np
import matplotlib.pyplot as plt
S, x, y = list(map(float, input().split()))
y=int(y)
A=[0]*12*y
Nomerok=[]
for i in range(1,12*y+1):
    Nomerok.append(i)
KapKap=[0]*12*y
Osnova=[0]*12*y
P=x/1200
S0=S
SS=S0
mecyac=12*y
RASPLATA=S*(P+P/((1+P)**mecyac-1))
RASPLATA=float(Decimal(RASPLATA).quantize(Decimal('0.01')))
print('Аннуительный платеж=', RASPLATA)
def Procenty(S,i):
    return Decimal(S*(1+x/100/12)).quantize(Decimal('0.01'))
for i in range (12*y):
    S=float(Procenty(S,i))*(1+P)
print('Переплата=',float(Decimal(S-S0).quantize(Decimal('0.01'))))
for i in range (12*y-1):
    A[i]=float(Decimal(SS*(1+P)-RASPLATA).quantize(Decimal('0.01')))
    SS=A[i]
    KapKap[i]=float(Decimal(A[i]*P).quantize(Decimal('0.01')))
    with localcontext(Context(len(str(A[i]//1))+2)):
        Osnova[i]=float(Decimal(RASPLATA)-Decimal(KapKap[i]))
Ezheplatezh=[RASPLATA]*(12*y-1)
Ezheplatezh.append(A[-2])
Osnova[-1]=RASPLATA
data = [A,
        Osnova,
        KapKap,
        Ezheplatezh]

outfile = open('Pisanina.txt', 'w')
ncolumns = len(data[0])
outfile.write('          ')
for i in range(1, ncolumns+1):
    outfile.write('%10s    ' % ('Месяц %2d' % i))
outfile.write('\n')
row_counter = 1
for row in data:
    if row_counter==1:
        outfile.write('Остаток  ')
    elif row_counter==2:
        outfile.write('Основной  ')
    elif row_counter==3:
        outfile.write('Проценты  ')
    else:
        outfile.write('Ежемес.пл.')
    for column in row:
        outfile.write('%14.8f' % column)
    outfile.write('\n')
    row_counter += 1
plt.plot(Nomerok,A)
plt.show()
plt.plot(Nomerok,KapKap)
plt.plot(Nomerok,Osnova)
outfile.close()
plt.show()



