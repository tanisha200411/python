"""Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects"""
# (ans) no the  output will intact nothing will change in it but it is not good practice to do so that's it .

# **********************************************************************************************
#Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoDVactor :

    def __init__(self , i , j):
        self.i = i
        self.j = j    

    def show(self):
        print(f"The 2D  vactor is {self.i}i + {self.j}j")     

class ThereeDVactor (TwoDVactor):

    def __init__(self,i, j, k):
        super( ).__init__(i,j)
        self.k = k

    def show(self):
      print(f"The 3D vactor is {self.i}i + {self.j}j + {self.k}k")     

a = TwoDVactor(1,2)
a.show()
b = ThereeDVactor(1, 2, 3)
b.show()


    
