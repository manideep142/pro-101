
class Atm:
    def _init_(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquriy(self):
        print("Your balance is: $100")

    def cashwithdrawl(self,amount)
        new-amount = 100-amount
        print("Your withdrawed: " str(amount) + "Your remaining balance is: "+ str(new_amount))

def main():
        name = input("What is your name")
        print("Hello, "+ name)
        cardname = input("Insert your card number: ")
        pin = input("Enter your pin: ")
        new_user = Atm(cardnumber,pin)

        print("Choose your activity")
        print("1. Balance Inquiry")
        print("2. Cash withdrawl")
        activity = int(input("Enter activity choice: "))

        if (activity == 1):
            new_user.balanceinquriy()
        elif (activity == 2):
            amount = int(input("Enter the amount: "))
            new_user.cashwithdrawl(amount)
        else:
            print("Enter a valid number")

if__name_=="_main_":
 main()


