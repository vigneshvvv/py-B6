class Employee:
    def __init__(self, id, firstName, lastName, emailID):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.emailID = emailID

class Developer(Employee):
    def __init__(self, id, firstName, lastName, emailID, techSkills):
        super().__init__(id, firstName, lastName, emailID)
        self.techSkills = techSkills

class Manager(Employee):
    def __init__(self, id, firstName, lastName, emailID, noOfProject):
        super().__init__(id, firstName, lastName, emailID)
        self.noOfProjects = noOfProject


dev = Developer(1, "Vignesh", "Kumar", "V@gmail.com", "Python")
print(dev.firstName)
print(dev.techSkills)
print(dev.__dict__)

manager = Manager(2, "Sathish", "Kumar", "Sathish@gmail.com", 5)
print(manager.__dict__)