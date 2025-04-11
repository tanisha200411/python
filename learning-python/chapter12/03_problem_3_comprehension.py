"""Write a list comprehension to print a list which contains the multiplication table of a
user entered number."""


n = int(input("Enter the number: "))
table = [n*i for i in range (1,11)]



""". Store the multiplication tables generated in problem 3 in a file named Tables.txt."""


with open("D:/python/learning-python/chapter12/tables.txt", "a") as f:
     f.write(f"Table of {n} : {(str(table)) } \n")





