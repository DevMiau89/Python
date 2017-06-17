#4. Write a Python program to reverse a string.
def str_reverse(s1):
   return "".join(reversed(s1))

print str_reverse("kulka")    

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
from math import factorial

def factorial_calculator(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)

print factorial_calculator(0)