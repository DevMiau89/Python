#26. Write a Python program to match if two words from a list of words starting with letter 'P'
import re

my_string = "puch to puc"

pattern = r"(p\w+)"

p = re.findall(pattern, my_string)

for i in p:
    print i



words = ["Python PHP", "Java JavaScript", "c C++"]

for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        # Check for success
        if m:
            print(m.groups())    