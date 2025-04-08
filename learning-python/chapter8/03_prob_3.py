"""
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 - year old.
"""
def generate_tables(n):
    table = ""
    for i in range (2,11):
        table += f"{n} X {i} = {n*i} \n"

    with open (f"D:/python/learning-python/chapter8/tables/table_{n}.txt", "w") as  f:
        f.write(table)


for i in range (2,21):
    generate_tables(i)
