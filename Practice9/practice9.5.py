__author__ = 'student'
Slova = open('xinput.txt','r')
Words = dict()
Stroka = Slova.readline()
while Stroka != '':
    Stroka = Stroka.rstrip()
    A=Stroka.split(' - ')
    Stroka=Slova.readline()
    if ',' in A[1]:
        B=A[1].split(',')
        print(B)
        for i in range (len(B)):
            Words[B[i]]=A[0]
    else:
        Words[A[1]]=A[0]
with open('output.txt','w'):
    while Words!={}:
        for subjects in Words:
            value = A.pop(subjects)
            print(value)
print(Words)