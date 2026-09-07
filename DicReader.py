import csv

with open("studentDetails.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        # print(row["name"])
        if int(row["Marks"]) > 200:
            print(row)