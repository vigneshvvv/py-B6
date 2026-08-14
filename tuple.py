t1 = (10,20,30, 40,50, 10)
print(t1[0])

# t1[0] = 15
# print(t1[0])

a = (10,)
#to find type
print(type(a))

#slicing tuple
print(t1[0:2])

#to find length of tuple
print(len(t1))

#to find number of element inside tuple
print(t1.count(10))

#find index of element in tuple
print(t1.index(20))

#to check number present in tuple
print(40 in t1)

#combining both tuple 
a = (1,2,3)
b= (3,4,5)
print(a+b)

print(max(t1))

student = (
    ("Vignesh", 25),
    ("Arun", 23),
    ("Sathish", 22)
)

#acessing nested tuple
print(student[0][0])

# converting tuple to list and list to append
sample = (120,122,123,124)
sample  = list(sample)
sample[1] = 121

sample = tuple(sample)
print(sample)

# appending value inside list in tuple
lst = (10,20,30, [40,50])
lst[3].append(60)

print(lst)


# //to compare two tuple
print(a == b)

st = "vignesh", 24, "PY"
print(st)

st1 = ("vignesh", 24, "PY")

name , age , course = st1
print(name)
print(age)
print(course)

st2 = (10,20,30,40,50)

first, *middle, end = st2
print(first)
print(middle)
print(end)