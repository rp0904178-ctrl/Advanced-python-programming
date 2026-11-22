import csv
import json

csv_file = "input.csv"
json_file = "output.json"

with open(csv_file, mode="r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open(json_file, mode="w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("CSV data JSON madhe convert zala:", json_file)
