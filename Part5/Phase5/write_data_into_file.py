"""Write data into a file."""

from pathlib import Path

FILE_PATH = Path("Part5/Phase5/hello_world.txt")
file_name = FILE_PATH.name


with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
    file_obj.write(
        "Hello Python! I am ready for job as python developer."+"\n"
    )
    print(f"Content written to {file_name} successfully.")
