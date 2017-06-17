#2. Write a Python program that matches a string that has an a followed by zero or more b's. 
from re import *

p = compile(r'[ab*]')
m = p.search("ac")

if m:
    print 'Match found'
else:
    print 'No match'