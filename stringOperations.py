text = "Welcome"

# print(text[0])
# print(text[-2])

# print(text[0:3])

# print(text[::-1])

# print(len(text))

first_name = "Vignesh"
last_name = "Kumar"

full_name = first_name + " " + last_name
# print(full_name)

# print(text *3)

textN = "We are coding python"

print("coding" in textN)

# print(textN.upper())
# print(textN.title())
# print(textN.capitalize())
# print(textN.swapcase())

textS = "##coding in python "
# print(textS.strip())
# print(textS.lstrip())
# print(textS.rstrip())

print(textS.strip("#"))

result = textN.replace(" ", "")
print(result)

resultN = textN.split()
print(resultN)

textN = "We,are,coding,python"
resultS = textN.split(",")
print(resultS)


resultJoin = "/".join(resultS)
print(resultJoin)

email = "Vignesh@gmail.com"
# print(email.partition("@"))

num = "123"
# print(num.isdigit())

num1 = "Python 123"
# print(num1.isalnum())

num2 = " "
# print(num2.isspace())
# print(num2.isupper())

textF = "S.Sathish"
# print(textF.removeprefix("S."))

textB = "Sample.csv"
# print(textB.removesuffix(".csv"))

name = "Sathish"
age = 25

# print("I'm %s and I am %s years old" %(name,age))
# print("I'm {} and I am {} years old".format(name, age))

print("Hello\npython")

print("Hello\tPython")
path = r"C:\\users\\Vignesh"

text = "python"

# for c in text:
#     print(c)

# for index, character in enumerate(text):
#     print(index, character)


