#10. Write a Python program that matches a word at the beginning of a string.
import re

my_string = "Owl eats mice and rats"

p = re.match(r'^\w', my_string)

if p:
    print "word matches"
else:
    print "word does not match"