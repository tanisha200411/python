#  Write a program to filter a list of numbers which are divisible by 5

def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a = [1 ,4,5 ,25,67,55,45,100,4680 , 6306730]

f = list(filter(divisible5,a))
print(f)