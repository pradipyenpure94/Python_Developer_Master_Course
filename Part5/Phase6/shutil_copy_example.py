"""Copy/Move files using shutil."""

import shutil

# Copy a file
SOURCE_FILE = "Part5/Phase6/read_json_file.py"
DESTINATION_FILE = "Part5/Phase6/read_json_file2.py"
# Copy content from one file to another file
shutil.copy(SOURCE_FILE, DESTINATION_FILE)

# Move a file
SOURCE_FILE = "Part5/Phase6/read_json_file2.py"
DESTINATION_FILE = "Part5/Phase6/read_json_file3.py"

shutil.move(SOURCE_FILE, DESTINATION_FILE)
