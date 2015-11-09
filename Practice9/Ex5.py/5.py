__author__ = 'student'
with open('input.txt', 'r') as inp:
    with open('ru-en.txt', 'w') as out:
        massive = []
        inpline = inp.readline()
        while inpline != '':
            inpline = inpline.split(' - ')
            inpline[1] = inpline[1].split('\n')[0]
            massive.append([inpline[0], inpline[1].split(', ')])
            inpline = inp.readline()
        print(massive)
        for x in massive:
            print(x)
        outdict = {}
        for i in range(len(massive)):
            for j in range(len(massive[i][1])):
                word = massive[i][1][j]
                if word not in outdict:
                    outdict[word] = massive[i][0]
                else:
                    outdict[word] += ', ' + massive[i][0]
        print()
        print(outdict)
        for x in outdict:
            print(x, '-', outdict[x])
        outmassive = []
        for x in outdict:
            outmassive.append([x, outdict[x].split(', ')])
        print()
        print(outmassive)
        for x in outmassive:
            print(x)
        for i in range(len(massive)-1):
            pass
