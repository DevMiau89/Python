#19 Write a python program to serach some literals string in a string.
import re

my_string = "Hello world. Hello 2.7 Python and JASON and JAVA"

patterns = ["Python", "JASON", "PHP"]

for pattern in patterns:
    print "Searching for {0} in {1}".format(pattern, my_string)
    if re.search(pattern, my_string):
        print "Pattern Matched"
    else:
        print "Not Matched"