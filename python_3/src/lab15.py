"""Lab 15.

* Change the previous program to allow, in addition to the normal
account, an account with a minimum balance. Do this through a
new class that inherits from the original. Make sure the new class
does the following:
* Provides for an initial deposit as well as a specified minimum balance
on account creation. For now, don't check to see that the initial
deposit meets the minimum requirement.
* Does not permit a withdrawal that takes the balance below the
minimum. Prints an error message instead.
* When an instance is printed, print the minimum as well as the
balance for minimum-balance accounts.
* Confirm that the deposit method works for the new class.
* Note - class variables are referenced through the original class
"""


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

a = BankAccount()
b = minBankAccount(100, 10)

a.withdraw(99)
b.withdraw(89)
b.withdraw(2)
