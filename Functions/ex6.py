#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst1):
    unique_elements = []
    for i in lst1:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements

print unique_list([1,2,3,3,3,3,4,5])    

#9. Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime_chceck(number):
    if number == 1:
        return False
    elif number == 2:
        True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
            return True
    

print prime_chceck(9)
         