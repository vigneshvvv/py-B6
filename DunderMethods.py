# __init__ -> constructor

class Student:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"StudentName: {self.name}"

    def __len__(self):
        return len(self.name)

# s1 = Student("Vignesh")
# print(s1)
# += 

# print(len("Hello"))

obj = Student(["Vignesh", "Sathish", "Ram"])
print(len(obj))

