__author__ = 'student'
class Matrix:

    def __init__(self,m,n=None):
        if isinstance(m,list):
            self.a=m
            for i in range(len(self.a)):
                if isinstance(self.a[i],list):
                    pass
                else:
                    print('Input correct matrix')
                    break

        else:
            try:
                self.a=[[0] * m for i in range (n)]
            except ValueError as e:
                print('Input correct value')


    def __add__(self,other):
        try:
            for i in range(len(self.a[0])):
                for j in range(len(self.a)):
                    self.a[i][j] += other.a[i][j]

        except ValueError as e:
            print('Input correct value')


    def set(self,i,j,value):
        self.a[i][j]=value


    def __eq__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            for i in range(len(self.a[0])):
                for j in range(len(self.a)):
                    if self.a[i][j]==other.a[i][j]:
                        pass
                    else:
                        return False
            return True
        else:
            return False


    def get_m(self):
        return len(self.a)


    def get_n(self):
        return len(self.a[0])


    def get_size(self):
        return len(self.a),len(self.a[0])
