from functools import reduce

employees = [
    {"name": "Vignesh", "Salary": 40000, "bonus": 4000},
    {"name": "Sathish", "Salary": 30000, "bonus": 4000},
    {"name": "Rahul", "Salary": 50000, "bonus": 4000}

]

result = sorted(employees, key=lambda employee: employee["name"])
print(result)

salaries = [30000, 40000,50000]
result1 = any(salary > 50000 for salary in salaries)
result2 = any(employee["Salary"] > 50000 for employee in employees)

result3 = all(employee["Salary"] > 20000 for employee in employees)
print(result1)
print(result2)
print(result3)

names = ["Ashok", "Arun", "Deva"]
salary = [60000, 30000,50000]
result4 = zip(names, salary)

print(list(result4))

for index, name in enumerate(names):
    print(index, name)


total_bonus = reduce(lambda total, employee: 
            total + employee["bonus"], employees, 0)

print(total_bonus)


