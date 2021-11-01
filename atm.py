import random
class Atm:
    def __init__(self, card, pin):
        self.card= card 
        self.pin= pin
    
    def cashWithdrawl(self):
        input("Enter your pin: ")
        print("Money withdrawn successfuly")
    
    def BalanceEnquiry(self):
        input("Input account number: ")
        print("Your account balance is ", random.randint(1000000, 20000000) )

person1= Atm(2004200719751978, 1234)
person1.cashWithdrawl()