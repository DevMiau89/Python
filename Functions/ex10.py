def pascal_function(number_of_rows):
    print "1" 
    for i in range(1, number_of_rows +1):
        top = i
        bottom = 1
        char = 1
        for j in range(i+1):
            print "%d"% char,
            char = char * top/bottom
            top -= 1
            bottom += 1
        print ""

            
pascal_function(5)

#14. Write a Python function to check whether a string is a pangram or not.
from string import ascii_lowercase
def is_pangram(seq):
    alphabet = ascii_lowercase
    for char in alphabet:
        if char not in seq:
            return False
    return True

print is_pangram("The quick brown fox jumps over the lazy dog" )    