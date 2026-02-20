import csv

data = [
    {"id": 1, "name": "Ali", "age": 25},
    {"id": 2, "name": "Sara", "age": 30},
]

with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "age"])
    writer.writeheader()
    writer.writerows(data)

print("ETL completed: output.csv created")