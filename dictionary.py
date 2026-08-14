student = {}
students = dict()

student = {
    "name": "Vignesh",
    "Department": "CSE"
}

print(student["name"])

student["grade"] = "B"
student["Department"] = "ECE"

print(student)

student.update({
    "Department": "EEE",
    "city":"Chennai"
})

print(student)

grade = student.pop("state", 0)
print(student)

data = student.popitem()
print(data)
print(student)

del student["grade"]
print(student)

student.clear()
print(student)

print("salary" in student)

print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)


student1 = student
student1["Department"] = "CSE"
print(student)

student2 = student.copy()
student2["Department"]= "EEE"
print(student)
print(student2)