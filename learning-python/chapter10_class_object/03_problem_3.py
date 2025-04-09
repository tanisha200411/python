'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

# the answer is no because the object instance may replace it but it can not change class attribute
# which means if a = 0 assined in object and class contain a=4 . it may print 0 over 4 but can not change the value of a contain by class which is 4

# ***************************************************************************************************

"""Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways."""
from random import randint
class Train :
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self,  fro, to):
        print(f"Ticket is booked in train no. : {self.trainNo} from {fro} to {to}")
        

    def getstatus(self, ):
        print(f"Train no.: {self.trainNo} is running on time ")

    def getfare(self,  fro ,to):
        print(f"Ticket fare in train no. : {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(180324)
t.book("Rampur", "Delhi" )
t.getstatus( )
t.getfare("Rampur", "Delhi" )