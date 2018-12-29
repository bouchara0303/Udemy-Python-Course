from bank import bankAccount

#Create bank account object
bank = bankAccount('bank.json')

#Login to account
print("Please login to access your account.")
bank.login()

#List of options
options = ("View Balance", "Withdraw", "Deposit", "Exit")
lenOptions = len(options)

def bankOptions():
    #Shows options
    for index in range(0, lenOptions):
        print(str(index + 1) + ": " + options[index])

    try:
        #Prompts user
        choice = 0
        while choice not in (1,2,3,4):
            choice = int(input("Please select an option from the list above: "))

        if choice == 1:
            bank.getBalance()
        elif choice == 2:
            amount = int(input("Please enter the amount you'd like to withdraw: "))
            bank.withdraw(amount)
            bank.getBalance()
        elif choice == 3:
            amount = int(input("Please enter the amount you'd like to deposit: "))
            bank.deposit(amount)
            bank.getBalance()
        elif choice == 4:
            print("Thank you for banking with Bouchard Credit Union, have a nice day!")
            exit()


        #Prompts user
        again = 0
        while again not in (1,2):
            again = int(input("Would you like to continue using the app? Press 1 to continue and 2 to quit: "))
        if again == 1:
            bankOptions()
        elif again == 2:
            print("Thank you for banking with Bouchard Credit Union, have a nice day!")
            exit()
    #Accounts for non int-type inputs to both prompts
    except ValueError:
        print("You have entered an invalid option. Please try again!")
        bankOptions()

bankOptions()
