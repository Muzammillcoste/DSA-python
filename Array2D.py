from Array import Array


class Array2D:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = Array(rows)
        for i in range(rows):
            self.rows[i] = Array(cols)
        

    def calrows(self) -> int:
        return (len(self.rows))

    def calcols(self) -> int:
        return (len(self.rows[0]))

    def clear(self, value: int) -> None:
        for i in range(self.calrows()):
            self.rows[i].clear(value)

    def __setitem__(self,pos,value) -> None:
        '''give two number in form of tuple or list
        first value specify row and second one for col'''
        assert len(pos) == 2, "please pass tuple or list with row and col no"
        i = pos[0]
        j = pos[1]
        assert self.calrows() > i >= 0 and self.calcols() > j >= 0, 'invalid index'
        self.rows[i][j] = value

    def __getitem__(self, pos) -> None:
        assert len(pos) == 2, "please pass tuple or list with row and col no"
        i = pos[0]
        j = pos[1]
        assert self.calrows() > i >= 0 and self.calcols() > j >= 0, 'invalid index'
        return self.rows[i][j]

    def traverse(self):
        for i in range(self.calrows()):
            for j in range(self.calcols()):
                print(self.rows[i][j],end=',')
            print()
    


def add(mat1,mat2):
    if mat1.calrows()!=mat2.calcols():
        return None
    x=mat1.calrows()
    y=mat1.calcols()
    mat3=Array2D(x,y)
    for i in range(x):
        for j in range(y):
            mat3[i,j]=mat1[i,j]+mat2[i,j]
    return mat3.traverse() 




    
if __name__=='__main__':
    a1=Array2D(3,3)
    for i in range(3):
        for j in range(3):
            a1[i,j]=2*j+i
    a2=Array2D(3,3)
    for i in range(3):
        for j in range(3):
            a2[i,j]=2*j+i
    add(a1,a2)
