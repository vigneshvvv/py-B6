class Employee:
    def __init__(self, id, firstName, lastName, emailID):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.emailID = emailID

class Address:
    def __init__(self, state, city):
        self.state = state
        self.city = city

class Developer(Employee,Address):
    def __init__(self, id, firstName, lastName, emailID, state, city, skills):
        Employee.__init__(self,id, firstName, lastName, emailID)
        Address.__init__(self,state, city)
        self.skills = skills

dev = Developer(1, "Vignesh", "kumar", "V@gmail.com", "TN", "Chennai", "Python")
print(dev.__dict__)