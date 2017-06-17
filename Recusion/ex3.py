#4. Write a Python program to get the factorial of a non-negative integer.
def non_negative_int_value(value):
    if value == 1:
        return 1
    else:
        return value * non_negative_int_value(value -1)
 


print non_negative_int_value(3)

