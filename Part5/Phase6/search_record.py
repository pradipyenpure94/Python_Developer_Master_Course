"""Search record in CSV."""

from pathlib import Path
import csv

FILE_PATH = Path("Part5/Phase6/add_rows.csv")

search_name = "Pradip"

with open(file=FILE_PATH, mode="r", encoding="utf-8", newline="") as file_obj:
    reader = csv.DictReader(file_obj)
    for record in reader:
        if record.get("name") == search_name:
            print(f"{search_name} found.")
            break
    else:
        print(f"{search_name} not found.")
