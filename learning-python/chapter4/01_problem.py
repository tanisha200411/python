
# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "Clock " : "Tokei",
    "Mobile phone" : "Keitai" ,
    "Key" : "kagi",
    "notebook" : "noto",
    "Park" : "Kouen"
}
word = input("enter the word :")

print(f"the meaning of {word}  is : {words[word]}")