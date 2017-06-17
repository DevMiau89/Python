#15. Write a Python program to check the validity of password input by users.
import re

password = raw_input("Please enter your password: ")


checks = [
    re.search("[a-z]",password),
    re.search("[0-9]",password),
    re.search("[A-Z]",password),
    len(password) > 6,
    len(password) < 16,
    re.search("[$#@]", password),
]

valid = True
for check in checks:
    if not check:
        print "password invalid"
        valid = False
        break
    
if valid:
    print "Password is okay"
    
    
        
