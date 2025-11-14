"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars

Request = None
Balance = 1000000

def Is_Float(Request):
    try:
        float(Request)
        return True
    except ValueError:
        return False
  
def S_Variable(Balance):
    if float(Balance) > 1:
        return "s"
    elif float(Balance) < 1:
        return "s"
    elif float(Balance) == 1:
        return ""
    
def S_Variable(Request):
    if float(Request) > 1:
        return "s"
    elif float(Request) < 1:
        return "s"
    elif float(Request) == 1:
        return ""

print(f"Hello, welcome to the bank! You currently have {int(float(Balance))} dollar{S_Variable(Balance)}. You may check your balance, withdraw money, deposit money, or leave the bank.")
while True:
    Request = input(f"To check your balance, reply CHECK, to withdraw money, reply TAKE, to deposit money, reply GIVE, and to leave the bank, reply EXIT. ")
    if Request == ("CHECK"):
        if Balance % 1 == 0:
            print(f"You currently have {int(Balance)} dollar{S_Variable(Balance)}.")
        else:
            print(f"You currently have {(Balance)} dollar{S_Variable(Balance)}.")

    elif Request == ("TAKE"):
        while True:
            Request = (input("How much money would you like to withdraw? "))
            if Is_Float(Request) == False:
                print("Please enter a valid number.")
            elif float(Request) <= 0:
                print("Please enter a valid number.")
            elif Is_Float(Request) == True:
                if float(Request) > float(Balance):
                    print(f"You do not have {Request} dollar{S_Variable(Request)} in the bank. Please enter a valid number.")
                else:
                    Balance = Balance - float(Request)
                    break
        print(f"You have withdrawn {Request} dollar{S_Variable(Balance)} from your balance.")
    elif Request == ("GIVE"):
        while True:
            Request = (input("How much money would you like to deposit? "))
            if Is_Float(Request) == False:
                print("Please enter a valid number.")
            elif float(Request) <= 0:
                print("Please enter a valid number.")
            elif Is_Float(Request) == True:
                Balance = Balance + float(Request)
                break
        print(f"You have deposited {Request} dollar{S_Variable(Request)} into your account.")
    elif Request == ("EXIT"):
        print("Thanks for visiting the bank. Hopefully we'll see you back here soon! Goodbye!")
        break
    else:
        print("Please enter a valid request.")