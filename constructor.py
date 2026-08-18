class userDetails:
    # id= 0
    # name = ""
    # city = ""

    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

user1 = userDetails(1, "Vignesh", "Chennai")
user2 = userDetails(2, "Sathish", "Madurai")
print(user1.__dict__)
print(user2.__dict__)