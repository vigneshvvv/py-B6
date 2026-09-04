employee = {
    "name": "Sathish",
    "age" : 25
}

updated_employee = {
    **employee,
    "salary": 60000
}

print(updated_employee)

a = [10,20]

b = [*a, 30,40]
print(b)