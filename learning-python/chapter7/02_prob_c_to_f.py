# Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    F = (9/5 * c) + 32.
    print(f"°F ={F}")

c = int(input("Enter the value of  celsius  : "))
celsius_to_fahrenheit(c)