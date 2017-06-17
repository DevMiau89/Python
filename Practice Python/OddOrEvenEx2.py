print "Please Enter your number: "
num = int(raw_input("> "))

print "Please Enter your first number: "
num1 = int(raw_input("> "))

print "Please Enter your second number: "
num2 = int(raw_input("> "))

if num % 2 == 0:
    print "\nYour number is even"
elif num % 4 == 0:
    print "\nYour number is a multiple of four"    
else:
    print "\nYour number is odd"

if num1 / num2 % 2 == 0:
    print "\nYour numbers divide evenly"
else:
    print "\nYour numbers do not divide evenly"   
