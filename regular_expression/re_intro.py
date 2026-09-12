"""Extract phone number from text."""

import re

text = "My phone 12 number is 9764837939."

result = re.search(r"\d{12}", text)
print(result.group())
