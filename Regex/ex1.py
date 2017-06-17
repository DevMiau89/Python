#1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re

email_address = 'wieczorek.karolina1@o2.pl'

searchObj = re.search(r'[a-zA-Z0-9.]', email_address, re.M | re.I)

if searchObj:
    print True
else:
    print False



"sxdupa1" -match '^sx|1$'