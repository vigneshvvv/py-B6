employees = [
    {"name": "Arun", "salary": 30000},
    {"name": "Deva", "salary": 50000},
    {"name": "Abdul", "salary": 70000},
    {"name": "Revanth", "salary": 90000}
]

updated_salary = map(
    lambda employee: employee["salary"] * 1.10, employees
)

eligble = [employee for employee in employees 
           if employee["salary"] >= 50000]

print(list(updated_salary))

print(eligble)

numbers = [10,20,30,40]
result = [number*2 for number in numbers]

print(result)

update_bonus = list(
    map(
        lambda employee: {
            **employee,
            "bonus": employee["salary"]*0.10
        }, employees
    )
)

print(update_bonus)