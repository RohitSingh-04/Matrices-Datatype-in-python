class Calculate:
    @property
    def transpose(self):
        #creating the zero matrix of same size
        trans_matrix=list()
        for i in range(self.column):
            trans_matrix.append([])
            for j in range(self.row):
                trans_matrix[i].append(0)
        #aab transpose kar ke naye zero matrix ko upodate krte hai
        for i in range(self.row):
            for j in range(self.column):
                trans_matrix[j][i]=self.matrix[i][j]
        #now making another object
        trans=Matrices.fromprogramitself(self.row, self.column, trans_matrix)
        return trans#returning the object
    
    def __len__(self):
        '''this function gives the number of element in the matrix'''
        return self.row*self.column
    def __add__(self, another):
        #checking for matrix compatible for addition
        if self.row==another.row and self.column==another.column:
            #now adding algo
            addedmatrix=[]
            for i in range(self.row):# i is the number for representing a row and will use it as index
                #inserting the blank list at index i
                addedmatrix.insert(i, [])
                for j in range(self.column):#j is the number for representing a column and will use it as index
                    # inserting added elements to the list
                    sum_element=self.matrix[i][j]+another.matrix[i][j]
                    addedmatrix[i].insert(j, sum_element)
            add=Matrices.fromprogramitself(self.row, self.column, addedmatrix)
        return add
    def __sub__(self, another):
        #checking for matrix compatible for addition
        if self.row==another.row and self.column==another.column:
            #now adding algo
            addedmatrix=[]
            for i in range(self.row):# i is the number for representing a row and will use it as index
                #inserting the blank list at index i
                addedmatrix.insert(i, [])
                for j in range(self.column):#j is the number for representing a column and will use it as index
                    # inserting subtracted elements to the list
                    sub_element=self.matrix[i][j]-another.matrix[i][j]
                    addedmatrix[i].insert(j, sub_element)
            sub=Matrices.fromprogramitself(self.row, self.column, addedmatrix)
        return sub
    def __mul__(self, another):
        #checking eligibility
        if self.column==another.row:
            resultant_matrix=[]
            sum=0
            #appending blank rows in a matrix
            for i in range(self.row):
                resultant_matrix.append([])
            for i in range(self.row):
                for j in range(another.column):
                    for k in range(self.row):
                        sum+=self.matrix[i][k]*another.matrix[k][j]
                    resultant_matrix[i].append(sum)
                    sum=0
            multiply=Matrices.fromprogramitself(self.row,another.column,resultant_matrix)
            return multiply
    def __truediv__(self, another):
        print( "Division of Matrix is not Possible")
        
class Type:
    def check_by_loop(self):
        #check for zero matrix
        result = 1# let the matrix is zero
        for i in self.matrix:
            for j in i:
                if j!=0:
                    result = 0# hence it is not 
        if result==1:
            return "Zero Matrix"
        #check for diagonal matrix and identity
        result = 0# let the matrix is not diagonal
        for i in range(self.row):#for the index of rows
            for j in range(self.column):#for the index of column
                if self.matrix[i][j]==0 and i!=j:#agar baki ke element zero hai to
                    result= 1#ho sakta hai ki matrix diagonal ho
                if self.matrix[i][j]!=0 and i==j:#agar diagonal element zero nahi hai to
                    result=1#yeh surely ek Diagonal matrix ho skti hai ya fir identity
                else:
                    result=0#agar upar ke do satisfy nahi hue to ye na hi diagonal matrix hai aur na hi identity
        if result==1:#agar proibabilityy hai ki ye matrix in do mai se ek he
            '''we have already checked for diagonal so may be it can be Identity so checking if it is one'''
            for i in range(self.row):#for the index of rows
                for j in range(self.column):#for the index of column
                    if self.matrix[i][j]==1 and i==j:#agar diagonal element 1 hai to vo identity hai
                        result=2
                    else:
                        result=1#surely diagonal hai
            if result==2:
                return "Identity Matrix"
            return "Diagonal Matrix"
        

    @property
    def type(self):
        other=self.check_by_loop()
        if self.row==1 and self.column!=1:
            return "Row Matrix"
        elif self.column==1 and self.row!=1:
            return "Column Matrix"
        elif self.row==1 and self.column==1:
                return "Singleton Matrix"
        elif self.row==self.column:
            if other != None:
                return f"Square Matrix and {other}"
            else:
                return "Square Matrix"
        elif self.row!=self.column:
            if other != None:
                return f"Rectangular Matrix and {other}"
            else:
                return "Rectangular Matrix"
        return self.check_by_loop()
        
class Matrices(Calculate, Type):
    def __init__(self, row, column, matrix_lis=[]):
        
        self.matrix=[]#for inserting the values further or if program want to initilize
        
        self.row, self.column =row, column #initlizing the row and column of that matrix
        
        #checking the validity for a matrix it shound not be 0X0
        if row == 0 or column ==0:
            print("matrix of 0X0 is invalid!")
            return 1
        if matrix_lis==[]:
             for i in range(self.row):# i is the number for representing a row and will use it as index
                #inserting the blank list at index i
                self.matrix.append([])
                j=0#use it as index
                while j<self.column:#j is the number for representing a column and will use it as index
                    #printing the message increminting i and j because in mathematics we represent matrix from 1 1
                    print("enter the row {} column {} element:> ".format(i+1,j+1))
                    item=input()#taking input
                    #checking for valid element
                    if item.isnumeric():
                        item=int(item)
                    else:
                        print("invalid input! assign something else!")
                        continue
                    #inserting the elements in the blank list
                    self.matrix[i].append(item)
                    j+=1#increment j
            
        else:
            self.matrix=matrix_lis

    @classmethod
    def fromprogramitself(cls, row, column, matrix):
        return cls(row, column, matrix)
    @classmethod
    def fromxstr(cls,string):
        '''this function takes input in form of rowXcolumn or rowxcolumn'''
        item_lis=string.split("x" or "X")
        try:
            item_lis=map(int, item_lis)
            int_item_lis=[i for i in item_lis]
        except ValueError:
            print("invalid input given!")
        return cls(int_item_lis[0], int_item_lis[1])
    @property
    def show(self):
        '''this function is to  show the matrix'''
        matrix=""
        for row in self.matrix:
            for column in row:
                matrix+=str(column)+"\t"
            matrix+="\n"
        matrix+=f"\t\t\t{self.row}x{self.column}"
        return matrix
    @property
    def order(self):
        '''this function returns the order of matrix'''
        return f"{self.row}x{self.column}"
    

if __name__ == "__main__":
    #testing
    # a=Matrices.fromxstr("3x3")
    # print(a.show)
    # print(len(a))
    # # print(a.matrix)
    # print("_"*30, "for b")
    # b=Matrices(3,3)
    # # print(b.matrix)
    # print(b.show)
    # c=a*b
    # print(c.show)
    # d=a-b
    # print(d.show)
    a=Matrices(2,2)
    print(a.type)
    at=a.transpose
    c=a/at
    # print(a,at)
    print(a.show)
    print(at.show)
    print(a.__dir__())#returns all the methods
