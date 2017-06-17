#12. Write a Python program that matches a word containing 'z'.
import re

my_string = "My owlz likes me and is now zzz."

p = (re.search(r'\w*z.', my_string))

if p:
    print "found a match!"
else:
    print "Not matched!"