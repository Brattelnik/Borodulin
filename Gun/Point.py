__author__ = 'Borodulin'
import math
class Point:
    x=0
    y=0
    def __init__(self, str):
        self.x,self.y = str.split(',')
        self.x,self.y = int(self.x), int(self.y)
    def __str__(self):
        return 'Point(' + str(self.x) +', ' + str(self.y)+ ')'
    def Distance(self):
        return math.sqrt(self.x**2 +self.y**2)
    def X(self):
        return(self.x)
    def Y(self):
        return(self.y)
    def Perimetr(self, other1,other2):
        return math.sqrt((self.x - other1.x)**2 + (self.y - other1.y)**2)+math.sqrt((other2.x - other1.x)**2 + (other2.y - other1.y)**2)+math.sqrt((self.x - other2.x)**2 + (self.y - other2.y)**2)

N=int(input())
Points=[]
SummaX=0
Perimetr=0
SummaY=0
for i in range (N):
    Points.append(Point(input()))
Max_distance = Points[0].Distance()
Furthest_point =Points[0]
for i in range(N):
    if Points[i].Distance() > Max_distance:
        Furthest_point=Points[i]
        Max_distance=Points[i].Distance()
    SummaX +=Points[i].X()
    SummaY +=Points[i].Y()
    for j in range(i,N):
        for k in range(j,N):
            Peri=Perimetr(Points[i],Points[j],Points[k])
            if Peri>Perimetr:
                Perimetr=Peri





print('Furthest point is ',str(Furthest_point))
print('Center of mass (',SummaX/len(Points),',',SummaY/len(Points),')')
print(Perimetr)




