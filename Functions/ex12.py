#16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def square(number):
    l = [i*i for i in xrange(1, number)]
    return l

print square(21) 

#17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.     
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def makeunderline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped       

@makebold
@makeitalic
@makeunderline
def hello():
    return "hello world"

print hello()