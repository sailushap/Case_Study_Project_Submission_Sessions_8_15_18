class piggy_bank:
    def __init__(self):
        self.balance = 0
    def add_Money(self,amount):
        if amount < 0:
            print("Amount cannot be negative")
        else:
            self.balance += amount
            print("Your current balance after adding", amount, "is", self.balance)
            #return self.balance
    def get_balance(self):
        print("Your current balance is:", self.balance)
    def withdraw_Money(self,amount):
        if amount < 0:
            print("Amount cannot be negative")
        elif (self.balance - amount < 0):
            print("Amount exceeds your current balance")
        else:
            self.balance -= amount
            print("Your current balance after withdrawing", amount, "is", self.balance)
            #return self.balance