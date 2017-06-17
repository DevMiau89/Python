#25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
import re

my_string = "2017-06-05"

replace = re.sub(r"(\d{1,4})-(\d{1,2})-(\d{1,2})", r"\3-\2-\1", my_string)

print replace