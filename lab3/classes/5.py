class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self, getmoney):
        if self.balance >= getmoney:
            self.balance -= getmoney
        else:
            print('you are not have enough money')
    def showBalance(self):
        print(self.balance)

owner = input()
balance = int(input())

putMoney = int(input())
getMoney = int(input())
b = Account(owner, balance)
b.showBalance()



b.deposit(putMoney)
b.showBalance()

b.withdraw(getMoney)
b.showBalance()

