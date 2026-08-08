ls = [10,20,40,50]
print(ls[0])
# print(ls[1])
# print(ls[2])
# print(ls[3])

ls[2] = 30
print(ls)

ls.append(60)
print(ls)

ls.insert(3, 40)
print(ls)

print(len(ls))

# print(ls[6])

print(ls[-1])
print(ls[len(ls)-1])
print(ls[-2])

ls.remove(60)
print(ls)

i = ls.index(20)
print(i)


lst = [30,10,40,20]
lst.sort()
print(lst)

numbers = list()
numbers.append(120)
print(numbers)

print(70 in ls)
if(40 in ls):
    print("Number exist")
else:
    print("number doesn't exist")

ls.reverse()

print(ls)

removed = ls.pop()
print(removed)
print(ls)

removes = ls.pop(0)
print(removes)

content = [10 , "Deva", 25000, True]

list1 = [10,20]
list2 = [30,40]
list3 = list1+list2
print(list3)

list1.extend(list2)
print(list1) 
