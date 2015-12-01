__author__ = 'student'
enru=open('en-ru.txt','r')
ruen=open('ru-en.txt','r')

Words=dict()
WordsNerds=dict()
Stroka=ruen.readline()
English=[]
Russian=[]
while Stroka!='':
    Stroka=Stroka.rstrip()
    A=Stroka.split(' - ')
    Stroka=ruen.readline()
    Words[A[1]]=A[0]
    English.append(A[1])
    Russian.append(A[0])
Stroka=enru.readline()
while Stroka!='':
    Stroka=Stroka.rstrip()
    A=Stroka.split(' - ')
    Stroka=enru.readline()
    WordsNerds[A[1]]=A[0]
    if A[0] not in English:
        English.append(A[0])
    if A[1] not in Russian:
        Russian.append(A[1])
with open ('output.txt','w'):
    if len(WordsNerds)==len(English):
        for i in range (len(English)):
            if English[i] in Words:
                print(English[i])
                print(Words[English[i]])
                print(English[i],' - ',Words[English[i]])
close('output.txt')



print(Words)
print(WordsNerds)
print(Words['home'],Words['mouse'])
print(English)
print(Russian)



