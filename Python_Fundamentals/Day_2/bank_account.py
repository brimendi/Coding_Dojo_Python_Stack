class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []

    def __init__(self, int_rate, balance): 
        # (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount): # increases the account balance by the given amount
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount): # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        self.balance = self.balance - amount 
        return self 

    def display_account_info(self): # print to the console: eg. "Balance: $100"
        amount = "${:,.2f}".format(self.balance)
        print(f"Balance: {amount}")
        return self

    def yield_interest(self): # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self 

    #class method to print all instances 
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            print("Balance: ${:,.2f}".format(account.balance))
        

#Create 2 accounts
brignies_account = BankAccount(.035, 300.85)
kens_account = BankAccount(.021, 5000.78)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
brignies_account.deposit(400).deposit(200).deposit(100).withdraw(300).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
kens_account.deposit(3000).deposit(4080).withdraw(30).withdraw(100).withdraw(400).withdraw(2000).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.all_instances()