"""Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
present, a message without exiting the program must be printed prompting the same."""

def files () :
    try :
        with (
        open('1.txt', ) as f1,
        open('2.txt') as f2,
        open('3.txt') as f3
    ):
            print("all files are opened")

            content1 = f1.read
            content2 = f2.read
            content3 = f3.read
            return content1, content2, content3    
            

    except FileNotFoundError :
        print("!!any of these files are not present !!")

files()






