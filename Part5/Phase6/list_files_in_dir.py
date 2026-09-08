"""List of files in a directory."""

import os
from pathlib import Path

DIR_PATH = Path("Part5/Phase6")

for record in os.listdir(DIR_PATH):
    file_path = os.path.join(DIR_PATH, record)
    if os.path.isfile(file_path):
        print(record)
