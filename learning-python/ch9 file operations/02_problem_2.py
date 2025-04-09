# Write a program to find out whether a file is identical & matches the content of
# another file.

file_path = "D:/python/learning-python/ch9 file operations/this.txt"
with open (file_path, "r",encoding= "utf-8") as f :
    content1 = f.read()

with open (file_path , "r" ,encoding= "utf-8") as f:
    content2 = f.read()

if (content1 == content2):
    print("Both the file is identical :)")    
else:
    print("No they do not share same content !")
        