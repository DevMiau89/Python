#15. Write a Python program where a string will start with a specific number. 
from re import *

my_string = "2-2345861"    
pattern = compile("^2")
    
z = pattern.match(my_string)

x =  z.span() 

print x