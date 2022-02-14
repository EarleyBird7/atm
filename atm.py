class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber 
        self.pin=pin
    def check_balance(self):
        print("your balance is 50000")
    def withdraw(self, amount):
        newAmount=50000-amount
        print("your have withdrawn amount"+str(amount)+"your remaining balance is"+str(newAmount))
def main():
    cardNumber=input("enter your card number")
    pinNumber=input("enter your pin number")
    newUser=Atm(cardNumber,pinNumber)
    print("choose any activity")
    print("1: balance 2: withdraw")
    activity=int(input("enter the number"))
    if(activity==1):
        newUser.check_balance()
    elif(activity==2):
        amount=int(input("enter the amount"))
        newUser.withdraw(amount)
if __name__=="__main__":
    main()
