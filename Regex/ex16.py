#20 Write a python program to search a literals in a string and also find the location within the original string where the pattern occurs.
import re

my_string = "Hello world. Hello 2.7 Python and JASON and JAVA"

patterns = (r"Python|JASON|PHP")

for m in re.finditer(patterns, my_string):
    print "{0}-{1}: {2}".format(m.start(), m.end(), m.group())

    
 