class User:
    def __init__(self, user_id, username):
        self.id = int(user_id)
        self.username= username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(input("What is your id? "), input("What is your name? "))
print(f"Your user id is: {user1.id} and \nYour username is: {user1.username}")

user2 = User(input("what is your id? "), input("What is your name? "))
print(f"Your user id is: {user2.id} and \nYour username is {user2.username}")

user1.follow(user2)
user2.follow(user1)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)


# user1 = User()
# user1.id = "001"
# user1.username = "homerdarang"
# print(f"Your id is {user1.id}")
# print(user1.username)


# user2 = User()
# user2.id = "002"
# user2.username = "jennykeece"
# print(f"Your is {user2.id}")
# print(user2.username)

# user3 = User()
# user3.id = "003"
# user3.username = "harrietjane"
# print(f"Your id is {user3.id}")
# print(user3.username)

# user4 = User()
# user4.id = "004"
# user4.username = "kalilinux"
# print(f"Your id is {user4.id}")
# print(user4.username)

# user5 = User()
# user5.id = "005"
# user5.username = "Jane"
# print(f"Your id is {user5.id}")
# print(user5.username)

# user6 = User(6)
# print(user6.seats)
