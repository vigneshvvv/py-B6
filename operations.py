a = int(input("Enter a Number A: "))
b = int(input("Enter a Number B : "))
operation = input("Enter a operation to perform 1. Add 2. Sub 3. Multiplication 4. Division")

if operation == "1":
    print(a+b)
elif operation == "2":
    if a > b:
        print(a-b)
    else:
        print("Printing Negative Value ", a-b)
        print(f"printing {a-b} negative value")
elif operation == "3":
    print(a*b)
elif operation == "4":
    print(a/b)
else:
    print("Invalid operation")