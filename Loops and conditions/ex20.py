#34. Write a Python program to check a triangle is valid or not. 

side1 = int(raw_input("Please enter the length of side1: "))
side2 = int(raw_input("Please enter the length of side2: "))
side3 = int(raw_input("Please enter the length of side3: "))

if side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2:
    print "Triange is valid"
else:
    print "Triange is not valid"    

#35. Write a Python program to check a string represent an integer or not. 
import re
user_input = raw_input("Please enter a string: ")

if not user_input.isdigit():
    print "The string is not an integer."

if re.search("[0-9]", user_input):
    print "The string is an integer."
else:
    print "The string is not an integer."    