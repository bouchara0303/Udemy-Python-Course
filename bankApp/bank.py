import json

class bankAccount:
    def __init__(self, filePath):
        self.filePath = filePath
        with open(filePath, 'r') as bFile:
            self.bankRecord = json.load(bFile)
        self.loggedIn = False
        self.userID = ''

    def login(self):
        userID = str(input("Please enter your user ID: "))
        password = input("Please enter your password: ")
        if userID in self.bankRecord:
            if password == self.bankRecord[userID]['password']:
                self.loggedIn = True
                self.userID = userID
            else:
                print('You have entered an incorrect Username/Passsword...')
                self.login()
        else:
            print('You have entered an incorrect Username/Passsword...')
            self.login()

    def getBalance(self):
        if self.loggedIn:
            print("Current Balance: $" + str(self.bankRecord[self.userID]['balance']))
        else:
            self.login()

    def deposit(self, amount=0):
        if self.loggedIn:
            if amount < 0:
                amount = int(input('Please enter a valid amount: '))
                self.deposit(amount)
            else:
                self.bankRecord[self.userID]['balance'] = self.bankRecord[self.userID]['balance'] + int(amount)
                with open(self.filePath, 'w') as outfile:
                    json.dump(self.bankRecord, outfile)
        else:
            self.login()

    def withdraw(self, amount=0):
        if self.loggedIn:
            if amount < 0:
                amount = int(input('Please enter a valid amount: '))
                self.withdraw(amount)
            elif amount > self.bankRecord[self.userID]['balance']:
                amount = int(input('Insufficient funds... Please enter a valid amount: '))
                self.withdraw(amount)
            else:
                    self.bankRecord[self.userID]['balance'] = self.bankRecord[self.userID]['balance'] - amount
                    with open(self.filePath, 'w') as outfile:
                        json.dump(self.bankRecord, outfile)
        else:
            self.login()
