#42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

while True:
    num1 = float(raw_input("Please enter first number: "))
    num2 = float(raw_input("Please enter second number: "))
    if num1 != 0 or num2 !=0:
        result = (num1 + num2)/ 2
        print "Your average is:", result
    else:
        break    
