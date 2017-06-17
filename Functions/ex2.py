#2. Write a Python function to sum all the numbers in a list.
def sum_numbers(list1):
    sum_of_numbers = sum(i for i in list1)
    return sum_of_numbers

print sum_numbers([1, 3, 5, 7])    

#3. Write a Python function to multiply all the numbers in a list. 
def multiply_numbers(list1):
    mul_of_numbers = 1
    for i in list1:
        mul_of_numbers *= i
    return mul_of_numbers

print multiply_numbers([1, 3, 5])
