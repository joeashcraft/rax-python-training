"""Lab 18 - module file"""


class BankAccount(object):  # Top tier class (super class)
    acct_cntr = 0  # class variable

    def __init__(self):   # This method runs during instantiation
        self.balance = 0  # instance variable
        BankAccount.acct_cntr += 1  # accessing a class variable

    def __del__(self):
        BankAccount.acct_cntr -= 1

    def __eq__(self, other):
        print '__eq__ method entered'
        if self.balance == other.balance:
            return True
        return False

    def __str__(self):
        print '__str__ method entered'
        return 'The balance for this account is ${:,.2f}'.format(self.balance)

    def withdraw(self, amount):  # a method
        self.balance -= amount
        return self.balance

    def deposit(self, amount):     # another method
        self.balance += amount
        return self.balance


class minBankAccount(BankAccount):
    def __init__(self, initial, minimum):
        if initial < minimum:
            raise ValueError('Initial balance is less than minimum balance.')
        self.balance = initial
        self.minimum = minimum
        BankAccount.acct_cntr += 1  # accessing a class variable

    def __str__(self):
        print '__str__ method entered'
        print 'Minimum Balance: {0:,.2f}'.format(self.minimum)
        return 'The balance for this account is ${:,.2f}'.format(self.balance)

    def withdraw(self, amount):  # a method
        if self.balance - amount < self.minimum:
            print 'FAIL: Account Balance would fall below Account Minimum.'
            return False
        self.balance -= amount
        return self.balance
