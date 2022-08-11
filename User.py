# Assignment: User
# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0

class User:
    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.already_rewards_member = True
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.


    def display_info(self):
        print("-----------------------")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Gold Points: {self.gold_card_points}")
        print("-----------------------")


# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def enroll(self):
        if self.is_rewards_member:
            print("User is already member")
            return
        self.is_rewards_member = True
        self.gold_card_points = 200

# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print ("You don't have enough points.")
            return

        self.gold_card_points -= amount


my_user = User("Thanh","Nguyen","TPNguyen@gmail.com", 28)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(50)
my_user.display_info()

second_user = User("John","Smith","JSmith@gmail.com", 31)
second_user.display_info()
second_user.enroll()
second_user.display_info()
second_user.spend_points(80)
second_user.display_info()

third_user = User("Sarah","Doe","SarahD@gmail.com", 26)
third_user.display_info()
third_user.enroll()
third_user.enroll()
third_user.display_info()
third_user.spend_points(250)
third_user.display_info()

# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.

from tkinter import E