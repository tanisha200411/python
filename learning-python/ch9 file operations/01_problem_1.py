# Write a program to make a copy of a text file “this. txt”
# Read the file using UTF-8 encoding
with open("D:/python/learning-python/ch9 file operations/this.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Write the content into a new file
with open("D:/python/learning-python/ch9 file operations/this_copy.txt", "w", encoding="utf-8") as f:
    f.write(content)

