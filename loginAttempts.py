userName = "Vignesh"
password = "Vignesh"

attempts = 1
isLoggedIn = False

while attempts < 4:

    userNameIn = input("Enter your userName: ")
    passwordIn = input("Enter your password: ")

    if userName == userNameIn and password == passwordIn:
        isLoggedIn = True
        break
    else:
        print(f"Either userName or password Incorrect Attempts remaining: {3-attempts}")
        attempts += 1

if isLoggedIn:
    print("Login successful")
else:
    print("Maximum attempt reached")