"""Write a program to print third, fifth and seventh element from a list using enumerate
function."""

l = ["naruto", "luffy", "kakashi", "sakura", "mikasa", "hinata", "akamaru", "zoro"]
# target_indexes = ([3,5,7])

# for index, value in enumerate(l):
#     if index in target_indexes:
#         print(f"Index {index}: {value}")
item = []
for i ,item in enumerate(l):
    if i == 3 or i == 5 or i == 7:
        print(item)
