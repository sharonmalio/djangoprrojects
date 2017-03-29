class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        self.balance -= withdraw


class SavingsAccount(BankAccount):
    def __init__(self, minimum_balance=500):
        self.balance = minimum_balance
        self.minimum_balance = minimum_balance


def deposit(self, deposit):
    if (deposit < 0):
        return "Invalid deposit amount"
    else:
        self.balance += deposit
        return self.balance


def withdraw(self, withdraw):
    # self.newbalance=self.balance-withdraw
    if (withdraw < 0):
        return "Invalid withdraw amount"
    elif self.balance - withdraw < self.minimum_balance:
        return "Cannot withdraw beyond the minimum account balance"
    elif (withdraw > self.balance):
        return("Cannot withdraw beyond the current account balance")
    else:
        self.balance -= withdraw
        return self.balance


class CurrentAccount(BankAccount):
    def __init__(self, minimum_balance=0):
        self.balance = minimum_balance

    def deposit(self, deposit):
        if (deposit < 0):
            print("Invalid deposit amount")
        else:
            self.balance += deposit
            return self.balance

    def withdraw(self, withdraw):
        if (withdraw < 0):
            print("Invalid withdraw amount")
        elif (withdraw > self.balance):
            print ("Cannot withdraw beyond the current account balance")
        else:
            self.balance -= withdraw
            return self.balance
