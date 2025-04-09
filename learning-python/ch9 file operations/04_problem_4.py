# Write a python program to rename a file to “renamed_by_ python.txt.

import os
file_path = "D:/python/learning-python/ch9 file operations/lets_wipe.txt"

old_name = "D:/python/learning-python/ch9 file operations/lets_wipe.txt"
re_name = "D:/python/learning-python/ch9 file operations/python.txt"

os.rename(old_name,re_name)

print("file re-named successfully :) ")


    
 