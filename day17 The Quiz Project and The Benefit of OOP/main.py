class User:
    # create class atribute
    # __init__ adalah atribute constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0  # define default attributes
        self.following = 0  # define default attributes

    def follow(self, user):
        user.followers += 1
        self.following += 1


# calling class atribute : Car(speed, fuel)
user_1 = User("001", "Decki Okmal Pratama")
user_2 = User("002", "Rasyid Gani")
# membuat attribute tambahan diluar class
user_1.likes = "Soccer"
user_2.likes = "Games"

print(user_1.__dict__)
print(user_2.__dict__)

user_1.follow(user_2)

print(user_1.__dict__)
print(user_2.__dict__)
