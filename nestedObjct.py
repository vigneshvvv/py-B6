class Coordinates():
    def __init__(self, lat,lng):
        self.lat = lat
        self.lng = lng

class Address():
    def __init__(self,state, city, lat, lng):
        self.city = city
        self.state = state
        self.coordinates = Coordinates(lat, lng)

class Employee():
    def __init__(self, id, name, state, city, lat, lng):
        self.id = id
        self.name = name
        self.address = Address(state, city, lat, lng)

    def printF(self):
        print("funtion printing")


emp = Employee(1, "Vignesh", "TN", "Chennai", "-11.23232", "22.3232")
print(emp.__dict__)
print(emp.address.city)
print(emp.address.coordinates.lat)

emp.printF()