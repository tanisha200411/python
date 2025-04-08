# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file
file_path = "D:/python/learning-python/chapter8/donkey.txt"

def don():
    text = ""
    for i in range(10):
        text += "you are a donkey, don't you understand you bitch, gigantic ashole\n"
    with open(file_path, "w") as f:
        f.write(text)

# Generate content
don()

# Read the file content
with open(file_path, "r") as f:
    word = f.read()

# Words to be replaced
words_list = ["donkey", "ashole", "bitch"]

# Replace each word with #####
for bad_word in words_list:
    word = word.replace(bad_word, "#####")

# Write back the cleaned text
with open(file_path, "w") as f:
    f.write(word)

print("Replacement done!")
