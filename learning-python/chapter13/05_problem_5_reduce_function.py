#  Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce
l = [45,75,67,89,34,50,98,64,43,99]


def greater(a,b):
   return a if a>b else b 

print(reduce(greater,l))






