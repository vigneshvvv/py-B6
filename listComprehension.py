numbers = [1,2,3,4,5,6]
result =[]

for num in numbers:
    if num%2 == 0:
        result.append(num)

print(result)

resultN = [number for number in numbers if number %2 == 0]
print(resultN)

employees = [
    {"name": "Vignesh", "Salary": 40000, "bonus": 4000},
    {"name": "Sathish", "Salary": 30000, "bonus": 4000},
    {"name": "Rahul", "Salary": 50000, "bonus": 4000}

]

high_Salary = [employee["name"] for employee in employees if employee["Salary"] > 30000]
print(high_Salary)

bonus_Salary = [employee["Salary"]*1.10 for employee in employees if employee["Salary"] > 30000]
print(bonus_Salary)

result2 = ["Even" if number %2 == 0 else "Odd" for number in numbers]
print(result2)

numbers1 = [1,2,3]
numbers2 = [10,20,30]


resultS = []
for x in numbers1:
    for y in numbers2:
        resultS.append(x+y)

print(resultS)

resultB = [x+y for x in numbers1 for y in numbers2]
print(resultB)
