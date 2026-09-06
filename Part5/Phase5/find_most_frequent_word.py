"""Find most frequent word in a file."""

from pathlib import Path
from collections import Counter

FILE_PATH = Path("Part5/Phase5/hello_world.txt")

with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
    data = file_obj.read().split()
    most_frequent_words = Counter(data).most_common(n=1)[0][0]
    print(f"Most frequent words: {most_frequent_words}")
