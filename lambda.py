def calculate_bonus(salary):
    return salary*0.10

calculate_bonusN = lambda salary: salary*0.10

print(calculate_bonus(200000))
print(calculate_bonusN(200000))

calculate = lambda price,quantity: (price*quantity)+50

print(calculate(1000,5))

# calculate = lambda salary: bonus = salary*0.10
#                                     print(bonus)

def findNum(number):
    if(number %2 == 0):
        return "Even"
    else:
        return "ODD"

print(findNum(13))


result = lambda number: "Even" if number %2 == 0 else "odd"

print(result(20))