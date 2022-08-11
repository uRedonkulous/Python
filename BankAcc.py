class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount ) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

checking =BankAccount(.02, 2000)
savings =BankAccount(.05, 3000)

checking.deposit(50).deposit(100).deposit(500).withdraw(50).yield_interest().display_account_info()
savings.deposit(200).deposit(1000).withdraw(50).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()