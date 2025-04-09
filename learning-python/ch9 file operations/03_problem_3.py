#  Write a program to wipe out the content of a file using python.
file_path = "D:/python/learning-python/ch9 file operations/lets_wipe.txt"
with open (file_path ,"r") as f:
    content = f.read()

with open (file_path,"w") as f :
    pass