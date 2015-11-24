__author__ = 'student'
class Matrix:

    def __init__(self,m,n=None):
        self.n=n
        self.m=m
        if isinstance(m,list):
            for i in range (len(m)):
                if not isinstance(m[i],list):
                    raise ValueError()

            if n!=None:
                raise ValueError()
            self.a=m
        if isinstance(m,int) and isinstance(n,int):
            if m <= 0 or n <= 0:
                raise ValueError()
            self.a=[[0]*n for i in range(m)]
        else:
            raise ValueError()




    def __add__(self,other):
        if not(isinstance(self,Matrix) and isinstance(other,Matrix) and len(self.a)==len(other.a) and len(self.a[0])==len(other.a[0])):
            raise ValueError()
        self.c=[[0]*self.n for k in range(self.m)]
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                self.c[i][j]=self.a[i][j] + other.a[i][j]
        return self.c

    def set(self,i,j,value):
        if i<0 or j<0 or i>len(self.a[0]) or j>len(self.a):
            raise ValueError()
        self.a[i][j]=value

    def get_m(self):
        return len(self.a)


    def get_n(self):
        return len(self.a[0])


    def __eq__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix) and len(self.a)==len(other.a) and len(self.a[0])==len(other.a[0]):
            for i in range(len(self.a)):
                for j in range(len(self.a[0])):
                    if self.a[i][j]==other.a[i][j]:
                        pass
                    else:
                        return False
            return True
        else:
            return False





    def get_size(self):
        return len(self.a),len(self.a[0])
