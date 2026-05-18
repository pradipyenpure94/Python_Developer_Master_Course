"""Find highest marks."""

subjects = {
    "DSA": 99,
    "CN": 45,
    "OSA": 75,
    "TOC": 85
    }

highest_mark_subject = max(subjects.items(), key=lambda k: k[1])
print(f"Highest Subject marks: {highest_mark_subject}")
