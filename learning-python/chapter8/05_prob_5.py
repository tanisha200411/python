# Write a program to mine a log file and find out whether it contains ‘python'
with open("D:/python/learning-python/chapter8/log.txt") as f:
    lines = f.readlines()

lineno = 1
found = False

for line in lines:
    if "python" in line.lower(): 
        print(f"YES PYTHON IS PRESENT IN LINE NO. = {lineno}")
        found = True
    lineno += 1

if not found:
    print("NO PYTHON IS NOT PRESENT IN ANY LINE.")




        


        
    
