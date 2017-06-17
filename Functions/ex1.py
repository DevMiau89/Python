#1. Write a Python function to find the Max of three numbers.
def max_numbers(list1):
    z = sorted(list1)
    return z[-1]

print max_numbers([1, 5, 7, 2, 6, 4])
print "---------------"

def max_value(num1, num2, num3):
    max_num = num1
    if (num2 > max_num ) and (num2 > num3):
        max_num = num2
    elif num3 > max_num:
        max_num = num3
    return max_num

print max_value(5, 7, 8)         

def biggest (a, b, c):
    imax = a
    if (b > imax) and (b > c):
            imax = b
    elif (c > imax):
            imax = c
    return imax

#to test
print (biggest(5,6,7))