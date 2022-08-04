
class User: 
    amount = 0 

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name 
        self.email = email 
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email} ")
        print(f"Age: {self.age}")

        if self.is_rewards_member == False:
            print(f"{self.first_name} {self.last_name} is not a rewards member.")
        else:
            print(f"{self.first_name} {self.last_name} is a rewards member.")
            print(f"Gold card points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
        else: print(f"{self.first_name}, you are already a rewards member!")

    def spend_points(self, amount):
        if self.gold_card_points =< 10: 
            print("Your reward points are running low! Watch how you spend them.")
        elif self.gold_card_points == 0:
            print("You do not have any points left to spend.")
        elif amount > self.gold_card_points:
            print("You do not have enough rewards points.")
        else: 
            self.gold_card_points -= amount 
            print(f"{self.first_name}, you now have {self.gold_card_points} gold card points left to spend.")

brignie_user = User("Brignie", "Mendieta", "br@gmail.com", 23)
# brignie.display_info()
brignie_user.enroll()
# brignie_user.display_info()

ken_user = User("Ken", "Rodriguez", "ar@gmail.com", 37)
ken_user.enroll()
# ken_user.display_info()

brignie_user.spend_points(50)
# brignie_user.display_info()

ken_user.spend_points(80)
# ken_user.display_info()
# ken_user.enroll()

ken_user.spend_points(120)
ken_user.spend_points(3)
ken_user.display_info()
