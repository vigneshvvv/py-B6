class UserDetails:
    id = 0
    firstName = ""
    lastName = ""
    city = ""

user1 = UserDetails()
user1.id = 1
user1.firstName = "Vignesh"
user1.lastName = "Kumar"
user1.city = "Chennai"

user2 = UserDetails()
user2.id = 2
user2.firstName = "Sathish"
user2.lastName = "Kumar"
user2.city = "Madurai"

print(user1.firstName)
print(user2.firstName)
print(user1.__dict__)
print(user2.__dict__)