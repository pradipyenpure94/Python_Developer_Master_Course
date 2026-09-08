"""Create directory using os."""

import os

DIR_PATH = "Part5/Phase6/sample_folder"
# os.makedirs(DIR_PATH, exist_ok=True)
try:
    os.mkdir(DIR_PATH)
except FileExistsError as error:
    print(f"Error: {error}")
else:
    print("Directory created successfully.")
