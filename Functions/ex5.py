# 6.Write a Python function to check whether a number is in a given range.

def range_chceck(num):
    if num in range(0, 10):
        print "{0} is in the range".format(num)
    else:
        print "{0} is not in the range".format(num)

range_chceck(6)

#7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_test(word):
    upper_case = 0
    lower_case = 0

    for letter in word:
        if letter.isupper():
            upper_case += 1
        else:
            lower_case += 1
            
    print "Original word:", word        
    print "No. of Upper case characters :", upper_case
    print "No. of Upper case characters :", lower_case

string_test("Kotek")
