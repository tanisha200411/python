"""Write a class “Calculator” capable of finding square, cube and square root of a
numbeer"""
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} = {self.n * self.n}")

    def cube(self):
        print(f"The cube of {self.n} = {self.n * self.n * self.n}")

    def square_root(self):
        print(f"The square root of {self.n} = {self.n ** 0.5}")


# User input
n = int(input("Enter the value of n: "))
calculate = input("What do you want to calculate (square, cube, square root, all)? ").lower()

a = Calculator(n)

# Conditions
if calculate == "all":
    a.square()
    a.cube()
    a.square_root()

elif calculate == "square":
    a.square()

elif calculate == "cube":
    a.cube()

elif calculate == "square root":
    a.square_root()

else:
    print("Invalid choice!")










        

    