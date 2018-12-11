class Account:
    update_rate = 1
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)
    
    def update_balance(self):
        self.balance *= self.update_rate

class SavingsAccount(Account):
    update_rate = 1.15

class DebitAccount(Account):
    update_rate = 1.02
        


