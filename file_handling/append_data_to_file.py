"""Append Data to file."""


# Open file in append mode
with open("file_handling/sample_text.txt", mode="a",
          encoding="utf-8") as file_obj:
    # Append data to file
    file_obj.write("\nAdded new line.")
