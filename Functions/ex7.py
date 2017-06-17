#9. Write a Python function that takes a number as a parameter and check the number is prime or not.
def prime_num(number):
    division_counter = 0
    for i in xrange(1, number + 1):
        if number % i == 0:
            division_counter += 1

    if division_counter == 2:
        print "{0} is a prime number".format(number)
    else:
        print "{0} is not a prime number".format(number)     

prime_num(997)          

#10. Write a Python program to print the even numbers from a given list.

def even_nums(lst1):
    new_list = []
    for i in lst1:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print even_nums([1, 2, 3, 4, 5, 6, 7, 8])