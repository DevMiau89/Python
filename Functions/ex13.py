#18. Write a Python program to execute a string containing Python code.

code = "print 'Hello World'"
my_code = """
def multiply(x, y):
    return x * y

print 'Multiply of 2 and 3 is:',multiply(2, 3)
"""
exec code
exec my_code

print "-----------------------"
#19. Write a Python program to access a function inside a function.

def make_adder(x):
       def adder(y):
           return x+y
       return adder

print make_adder(2)(5)  

#20. Write a Python program to detect the number of local variables declared in a function.     
import unittest
def foo():
     x = 1
     y = 2

def bar():
    pass

print "----------------------"
print(foo.__code__.co_nlocals)
print(bar.__code__.co_nlocals)

