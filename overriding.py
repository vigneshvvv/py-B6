class Parant:
    def show(self):
        print("Parant method")

class Child(Parant):
    def show(self):
        print("Child Method")


ch = Child()
ch.show()