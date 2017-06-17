#3. Write a Python program to guess a number between 1 to 9.
from sys import exit

user_input = 0

while user_input != 7:
    print "Hello, please enter the number between 1 to 9"
    user_input = int(raw_input(">>> "))
    if user_input == 7:
        print "Congratulations you've won"
    else:
        print "Sorry you need to try again"
        print "Would you l ike to contiune?(Enter Y or N)"
        contiune = raw_input(">>> ")
        if contiune != "Y":
            exit()
            
