userName = "Vignesh"
password = "Vignesh"
attempts = 1

while attempts > 0 :

    if attempts > 3:
        print("Maximum attempts reached..please try again after sometime")
        break
    userNameN = input("Enter your UserName: ")
    passwordN = input("Enter your password: ")

    if userName == userNameN and password == passwordN:
        print("login successful")
        break
    else:
        print(f"Either userName or password is incorrect. Remaining attempts: {3-attempts}")
        attempts += 1
else:
    print("Login operation completed")