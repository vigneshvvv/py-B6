users = [{
    "userName":"Vignesh",
    "password": "Vignesh"
},
{
    "userName":"Sathish",
    "password": "Sathish@123"
},
{
    "userName":"Deva",
    "password": "Deva@321"
}
]


def loginUser():
    attempts = 1

    while(attempts > 0):
        if attempts == 4:
            print("Maximum attempts reached")
            break
        username = input("Enter your userName: ")
        password = input("Enter your password: ")

        isUserPresent = False

        for user in users:
            if user["userName"] == username and user["password"] == password:
                isUserPresent = True
                break

        if isUserPresent:
            print("login Successful")
            break
        else:
            print(f"either userName or password incorrect. Attempts remaining {3-attempts}")
            attempts +=1

def forgotPassword():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    reEnter = input("Re-Enter your password: ")

    if password == reEnter:
        users.append({
            "userName": username,
            "password": password
        })
        print(users)
        option = input("Do you want to login Y ? N")
        if option == "Y":
            loginUser()
        else:
            print("reset successful")
    else:
        print("Password doesn't match")



operation = input("Enter operation to perform 1.login 2.ResetPassword")

if operation == "1":
    loginUser()
elif operation == "2":
    forgotPassword()
else:
    print("Invalid operation")
            
