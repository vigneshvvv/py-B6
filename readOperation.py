with open("students.txt", "r") as file:
    # data = file.read(2)
    # data = file.readline()
    data = file.readlines()

    for s in data:
        print(s.strip())

with open("students.txt", "w") as file:
    file.write("Vinay\n")
    file.write("pradeep\n")


with open("students.txt", "a") as file:

    students = ["Vignesh\n", "Jimson\n"]
    # file.write("Abdul\n")
    file.writelines(students)
    print("Append completed")


