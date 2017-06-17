#16. Write a Python program to remove leading zeros from an IP address. 
from re import *
my_IP = "172.016.2504.1" 

pattern = compile(r"\w*0")
p = pattern.sub('', my_IP)

print p
print "----------------------"

#17. Write a Python program to check for a number at the end of a string.

str1 = "172.016.2504.1"

pattern = compile(r'\d$')

m = pattern.search(str1)

if m:
    print "number is found", m.group()
else:
    print "No number at the end"
    