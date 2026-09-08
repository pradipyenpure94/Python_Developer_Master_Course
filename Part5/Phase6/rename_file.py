"""Rename files using os."""

import os

DIR_PATH = "Part5/Phase6"
OLD_FILE_NAME = "sample_csv_file.csv"
NEW_FILE_NAME = "sample_file.csv"

OLD_FILE_PATH = os.path.join(DIR_PATH, OLD_FILE_NAME)
NEW_FILE_PATH = os.path.join(DIR_PATH, NEW_FILE_NAME)

os.rename(OLD_FILE_PATH, NEW_FILE_PATH)
print("Successfully renamed file.")
