class Account:
    def __init__(self,balance,accNo):
        self.balance=balance
        self.accNo=accNo
        
    def credit(self,amount):
        self.balance+=amount
        print(f"Your account credited rs {amount}")
        print(f"Your account balance is {self.showBalance()}")
    def debit(self,amount):
        yn=input("Do you want to debit money from your account (yes/no):- ")
        if (yn=="yes"):
            self.balance -=amount
            print(f"Your account debited rs {amount}")
            print(f"Your account balance is {self.showBalance()}")
        elif (yn=="no"):
            print(f"Your account balance is {self.showBalance()}")
        else :
            print("you entered a an invalid option please write (yes/no)")
        
    def showBalance(self):
        return self.balance
    
    
bal=int(input("Enter your acc balance:- "))
acc=input("Enter your account no. :- ")   
acc=Account(bal,acc)
acc.credit(int(input("Enter amount you want to credit:- ")))
acc.debit(int(input("Enter your amount you want to debit:- ")))
acc.showBalance()