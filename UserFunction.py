# declare a class and give it name User
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

print("Hello!")

user_ada = User()
print(user_ada.first_name)

user_2 = User()
print(user_2.last_name)