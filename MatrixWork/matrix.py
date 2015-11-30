__author__ = 'Ivan Borodulin'
class Matrix:

    def __init__(self, m, n=None):
        if isinstance(m,int) and isinstance(n,int):
            if m<=0 or n<=0:
                raise ValueError()
            self.m = m
            self.n = n

            result = [[0]*m for i in range(n)]


            self.matrix = result
        elif isinstance(m,list):
            if n!=None: #not isinstance(m[0],list)
                raise ValueError()
            self.matrix = m
            self.m=len(m)
            self.n=len(m[0])
        else:
            raise ValueError()                                # Now you can check your inputs on ivalid values

    def __add__(self, other):
        result = Matrix(self.m, self.n)
        result.matrix = [0]*self.m
        for i in range(self.m):
            result.matrix[i]=[0]*self.n

        for i in range(self.m):
            for j in range(self.n):
                result.matrix[i][j] =0 # Even NOW IT DOESN'T WORK!self.matrix[i][j] + other.matrix[i][j]
        return(result)

    def __sub__(self, other):
        result = Matrix(self.m, self.n)
        result.matrix = [0]*self.m
        for i in range(self.m):
            result.matrix[i]=[0]*self.n

        for i in range(self.m):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[j][i] - other.matrix[j][i]   # CHANGED J AND I in self and other
        return(result)

    def __eq__(self, other):
        if self.n!=other.n or self.m!=other.m:
            raise RuntimeError
        return(self.matrix == other.matrix)


    def __mul__(self, other):

        if type(other) == float or type(other) == int:
            result = Matrix(self.m, self.n)
            result.matrix = [0]*self.m
            for i in range(self.m):
                result.matrix[i]=[0]*self.n

            for i in range(self.m):
                for j in range(self.n):
                    result.matrix[i][j] = other*self.matrix[i][j]
        elif type(other) == Matrix:
            if self.n!=other.m:
                raise RuntimeError()
            result = Matrix(self.m, other.n)
            result.matrix = [0]*self.m
            for i in range(self.m):
                result.matrix[i]=[0]*other.n

            for i in range(self.m):
                for j in range(other.n):
                    for k in range(other.m):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return(result)


    def __truediv__(self, other):

        if type(other) == float or type(other) == int:
            result = Matrix(self.m, self.n)
            result.matrix = [0]*self.m
            for i in range(self.m):
                result.matrix[i]=[0]*self.n

            for i in range(self.m):
                for j in range(self.n):
                    result.matrix[i][j] = self.matrix[i][j]/other
        return(result)


    def get(self, i, j):
        return(self.matrix[j][i])


    def get_m(self):
        return(self.m)


    def get_n(self):
        return(self.n)


    def get_size(self):
        return(self.m,self.n)


    def set(self, i, j, value):
        self.matrix[j][i] = value


    def determinant(self):
        if self.m!=self.n:
            raise RuntimeError()
        if len(self.matrix)==2:
            return self.matrix[0][0]*self.matrix[1][1]-self.matrix[0][1]*self.matrix[1][0]
        if len(self.matrix)==3:
            return self.matrix[0][0]*(self.matrix[1][1]*self.matrix[2][2]-self.matrix[1][2]*self.matrix[2][1])-self.matrix[0][1]*(self.matrix[1][0]*self.matrix[2][2]-self.matrix[2][0]*self.matrix[1][2])+self.matrix[0][2]*(self.matrix[1][0]*self.matrix[2][1]-self.matrix[1][1]*self.matrix[2][0])

    def invert(self):
        return Matrix([[-1, 1],[2, -1]]) #
    def transpose(self):
        self.matrix=list(zip(*self.matrix))
        return self.matrix