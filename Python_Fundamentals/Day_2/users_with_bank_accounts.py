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
        

class User: 

    def __init__(self, name, email):
        self.name = name
        self.email = email 
        self.accounts = {}
        
    def add_account(self, name, int_rate):
        self.accounts[name] = BankAccount(int_rate, 0)

    def make_deposit(self, name, amount):
        account = self.accounts[name]
        account.deposit(amount)
        
    def make_withdrawal(self, name, amount):
        account = self.accounts[name]
        account.withdraw(amount)

    def display_user_balance(self, name):
        account = self.accounts[name]
        print(name)
        account.display_account_info()

    def display_all_user_balances(self):
        for account in self.accounts.values():
            account.display_account_info()
    
    def transfer_money(self, amount, account_name, other_user, other_account_name):
        self.make_withdrawal(account_name, amount)
        other_user.make_deposit(other_account_name, amount)

        



bri_user = User("Bri M", "br@gmail.com")
bri_user.add_account("checking", 0.05)
bri_user.make_deposit("checking", 100)
bri_user.make_withdrawal("checking", 25)
bri_user.display_user_balance("checking")

bri_user.add_account("savings", 0.25)
bri_user.make_deposit("savings", 1000)
bri_user.make_withdrawal("savings", 5)
bri_user.display_user_balance("savings")

bri_user.display_all_user_balances()

ken_user = User("Ken M", "km@gmail.com")
ken_user.add_account("savings", 0.5)
ken_user.make_deposit("savings", 10)
ken_user.display_user_balance("savings")


bri_user.transfer_money(90, "checking", ken_user, "savings")

ken_user.display_user_balance("savings")