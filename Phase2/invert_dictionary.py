"""Invert dictionary (swap key-value)"""

students = {"ajay": 100, "amit": 96}

inverted_dict = {v: k for k, v in students.items()}
print(f"Inverted dictionary: {inverted_dict}")
