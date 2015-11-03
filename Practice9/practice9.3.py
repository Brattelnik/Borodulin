__author__ = 'student'
Words = dict()
input=open('input.txt','r')
Stroki=input.readlines()
max=0
for i in range(len(Stroki)):
    Stroki[i]=Stroki[i].replace('.',' ')
    Stroki[i]=Stroki[i].replace(',',' ')
    Stroki[i]=Stroki[i].replace('?',' ')
    Stroki[i]=Stroki[i].replace('!',' ')
    Stroki[i]=Stroki[i].replace('-',' ')
    Stroki[i]=Stroki[i].lower()
    A=Stroki[i].split()
    for j in range(len(A)):
        if A[j] in Words:
            Words[A[j]]+=1
            if Words[A[j]]>max:
                max=Words[A[j]]
                maxi=A[j]
        else:
            Words[A[j]]=1
print(max,maxi)