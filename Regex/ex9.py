#11. Write a Python program that matches a word at end of string, with optional punctuation.
import re

theStr = "Owl eats everything and even more."

p = re.match(r'[a-zA-Z0-9]+$|[a-zA-Z0-9]+\.$', theStr)

if p:
    print "Word matches!"
else:
    print "No match found!"