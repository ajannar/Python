from random import randint

class Bank:

    def __init__(self):
        self.accounts = {"dummy123" : ["dummyUser","dummy123",1000]}

    def createAccount(self, name, password, initialBalance):

        while(True):
            self.accountID = name[:4] + str(randint(100,999))

            if self.accountID not in self.accounts.keys():
                break
        
        self.accounts[self.accountID] = [name, password, initialBalance]
        print()
        print("Hello",name,"your account is created successfully. Your account id is",self.accountID)

    def authenticate(self, accountID ):

        if accountID in self.accounts.keys():
            print()
            print("Enter password: ")
            password = input()

            if password == self.accounts[accountID][1]:
                print()
                print("Authentication successful. Welcome",self.accounts[accountID][0])
                self.accountID = accountID
                return True
            else:
                print()
                print("Password you entered is incorrect.")
                return False
        else:
            print()
            print("This account id does not exist.")
            return False

    def displayBalance(self):
        print()
        print("Your current account balance is",self.accounts[self.accountID][2])  

    def withdrawBalance(self,withdrawalAmount):

        if withdrawalAmount > self.accounts[self.accountID][2] :
            print()
            print("Insufficient funds.")

        elif withdrawalAmount <=0:
            print()
            print("Withdrawal amount can't be less than or equal to Zero")
        else:
            print()
            print("Withdrawal successful.")
            self.accounts[self.accountID][2] = self.accounts[self.accountID][2] - withdrawalAmount
            self.displayBalance()

    def depositBalance(self,depositAmount):
        if depositAmount <=0:
            print()
            print("Deposit amount can't be less than or equal to Zero")
        else: 
            self.accounts[self.accountID][2] = self.accounts[self.accountID][2] + depositAmount
            self.displayBalance()

bank = Bank()

print()
print("Welcome, dummy accountID and password is 'dummy123' with balance 1000")

while(True):
    print()
    print("Press 1 to login to your account")
    print("Press 2 to create new account")
    print("Press 3 to exit")

    userChoice = int(input())

    if userChoice == 1:
        print()
        print("Enter account id: ")
        accountID = input()

        if (bank.authenticate(accountID)) is True:
            while(True):
                print()
                print("Press 1 to display your account balance")
                print("Press 2 to withdraw money")
                print("Press 3 to deposit money")
                print("Press 4 to return to previous Menu")

                userOption = int(input())

                if userOption == 1:
                    bank.displayBalance()

                if userOption == 2:
                    print()
                    print("Enter amount you wish to withdraw: ")
                    withdrawalAmount = int(input())
                    bank.withdrawBalance(withdrawalAmount)

                if userOption == 3:
                    print()
                    print("Enter amount you wish to deposit: ")
                    depositAmount = int(input())
                    bank.depositBalance(depositAmount)

                if userOption == 4:
                    break

    if userChoice == 2:
        print()
        print("Enter name for your account: ")
        name = input()

        print()
        print("Set password for your account: ")
        password = input()

        print()
        print("Enter initial deposit amount: ")
        initialBalance = int(input())

        bank.createAccount(name, password, initialBalance)

    if userChoice == 3:
        quit()
        