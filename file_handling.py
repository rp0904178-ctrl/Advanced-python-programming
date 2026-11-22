import csv

students = [
    [101, "Rahul", 85],
    [102, "Priya", 92],
    [103, "Amit", 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["RollNo", "Name", "Marks"])

    writer.writerows(students)

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
