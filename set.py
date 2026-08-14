numbers = {10,10,20,30,30,40}
print(numbers)

# to create new empty set 
s = set()

# insert number on set
s.add(100)
print(s)

# to add multiple numbers
numbers.update([50,60,70])
print(numbers)

# gives error if number exist
# numbers.remove(80)
# print(numbers)

# safest way to remove elements without throwing error
numbers.discard(80)
print(numbers)

# to remove the first element 
removed = numbers.pop()
print(removed)
print(numbers)

# numbers.clear()
# print(numbers)

# to chec whether number exist 
print(30 in numbers)

a = {1, 2, 3}
b = {3,4,5}

# to find non repeating elements 
print(a | b)

# to find the repeating element alone 
print(a & b)

# unique elements on side of a
print(a - b)

# gives only unique elements between a and b
print(a ^ b)