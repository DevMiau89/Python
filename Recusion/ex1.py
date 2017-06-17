#1. Write a Python program to calculate the sum of a list of numbers

a_list = ([1, 2, 3, 4, 5])

x = 1
for i in range(len(a_list)):
    x *= a_list[i]

print x
print "--------------------"

def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)

print fact(5)


def factorial(number):
    x = 1
    for i in range(number):
        x = x * (i+1)
    return x

print factorial(5)        