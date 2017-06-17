#11. Write a Python function to check whether a number is perfect or not. 

def perfect_number(number):
    counter_modulus = 0
    for i in range(1, number):
        if number % i == 0:
            counter_modulus += i

    if number == counter_modulus:
        print "{0} is a perfect number".format(number)
    else:
        print "{0} is not a perfect number".format(number)

perfect_number(6)

#12. Write a Python function that checks whether a passed string is palindrome or not.

def palindrome_check(str1):
    new_str = ""
    for letter in reversed(str1):
        new_str += letter
    
    if new_str == str1:
        return True
    else:
        return False

print palindrome_check("poop")    

    
