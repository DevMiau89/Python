#21 Write a python program to find the substring within a string.
import re

my_string = "Python 2.7 exercises, C# exercises and JAVA"

pattern = "exercises"

match = re.findall(pattern,my_string)

for i in match:
    print i

