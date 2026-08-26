class Employee:
    def __init__(self, id, firstName, lastName, emailID):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.emailID = emailID

class Address(Employee):
    def __init__(self, id, firstName, lastName, emailID, state, city):
        super().__init__(id, firstName, lastName, emailID)
        self.state = state
        self.city = city

class Developer(Address):
    def __init__(self, id, firstName, lastName, emailID, state, city, skills):
        super().__init__(id, firstName, lastName, emailID, state, city)
        self.skills = skills

dev = Developer(1, "Vignesh", "kumar", "V@gmail.com", "TN", "Chennai", "Python")
print(dev.__dict__)