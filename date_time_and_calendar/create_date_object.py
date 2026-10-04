"""Convert string to date using strptime()."""

from datetime import datetime

date_string = "26-10-10"
date_object = datetime.strptime(date_string, "%y-%m-%d").date()
print(date_object)
