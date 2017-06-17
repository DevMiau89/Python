#8. Write a Python program to find sequences of one upper case letter followed by lower case letters.
import re

def match_text(string):
    p = re.search(r'^[a-z].*[A-Z]$', string, re.I | re.M ) 
    if p:
        print True, p.group()
    else:
        print False

match_text("Koci KoCi Lapki")

