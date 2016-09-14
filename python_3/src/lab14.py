"""Lab 13 - Class Example

When you compare, __cmp__ is called automatically and it will blindly compare two instances which will never be equal.

* To override __cmp__, implement one or more of the newer magic methods - in our case __eq__.

* Add this code to your program:
    def __eq__(self, other):
        print '__eq__ method entered'
        if self.balance == other.balance:
        return True
        return False
    a = BankAccount()
    b = BankAccount()
    a.deposit(2100)
    b.deposit(2100)
    if a == b:
        print 'The two accounts have the same balance'
    else:
        print 'The balances are different'
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


a = BankAccount()
b = BankAccount()
a.deposit(2100)
b.deposit(2200)
if a == b:
    print 'The two accounts have the same balance'
else:
    print 'The balances are different'


del b
print 'num of accounts -', BankAccount.acct_cntr
