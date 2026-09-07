import csv

# with open("studentDetails.csv", "a", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow([111, "Jimson", "ECE", 470])

st = [
    {
        "id": 112,
        "name": "Jack",
        "Department": "EEE",
        "Marks": 420

},
 {
        "id": 114,
        "name": "Daniel",
        "Department": "EEE",
        "Marks": 390

}

]

with open("studentDetails.csv", "a", newline="") as file:
    fieldName = ["id", "name", "Department", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldName)
    writer.writerows(st)