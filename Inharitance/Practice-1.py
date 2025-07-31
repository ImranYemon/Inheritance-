class TwoDvactor :
    def __init__(self , i , j):
        self.i = i
        self.j = j 
    
    def show (self):
        print(f"the value is {self.i}i + {self.j}j ")
        
class ThreeDvactor(TwoDvactor) :
    def __init__(self , i , j , k):
        super().__init__( i , j )
        self.k = k

    def show (self):
        print(f"the value is {self.i}i + {self.j}j + {self.k}k")

a = TwoDvactor(1,2)
a.show()
b = ThreeDvactor(1,2,3)
b.show()


