employees = [
    {"name": "Arun", "salary": 30000},
    {"name": "Deva", "salary": 50000},
    {"name": "Abdul", "salary": 70000},
    {"name": "Revanth", "salary": 90000}
]

eligble_employees = filter(lambda employee: employee["salary"] >= 50000, employees)

print(list(eligble_employees))