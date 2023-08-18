class ATM:
    def __init__(self,balance=0):
         self.balance = balance1

    def check_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self,amount):
        if 0 < amount <=self.balance:
            self.balance -= amount
            return True
        else:
            return False

def main():
    atm = ATM()

    while True:
        print("ATM Banking System")
        print("1.check balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exist")
        option=int(input("Enter your option:"))

        if option==1:
            print("Balance:",atm.check_balance())
        elif option==2:
            amount = float(input("Enter your amount to deposit:"))
            if atm.deposit(amount):
                print("Deposit successfull.Thank you")
            else:
                print("Invalid deposit amount")
        elif option==3:
            amount = float(input("Enter your withdraw amount:"))
            if atm.withdraw(amount):
                print("withdraw successfull and thank you for visit")
            else:
                print("insufficient funds")
        elif option==4:
            print("Thankyou for visiting and using atm bank system")
            break
        else:
            print("Invalid Option.please choose correct option")


if __name__ == "__main__":
    main()