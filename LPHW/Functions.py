def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(10, 20)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)

# Mistakes -> INDENTATION! 

def math_and_calculation(num1, num2):
    print "Number one equals %r" % num1
    print "Number two equals %r" % num2
    print "All looks nice!"
    print "Thank you!\n"



print "I am calling the function"
math_and_calculation(2, 5)

print "The result of addition is:"
math_and_calculation(10 + 5, 1 + 3)

print "I am declaring 2 new variables"
number1 = 6
number2 = 20

math_and_calculation(number1, number2)

print "Adding varibles and integers"
math_and_calculation(number1 + 10, number2 + 5)

print "Why don't you put your numbers:"
number1 = int(raw_input("Enter the first number: "))
number2 = int(raw_input("Enter the first number: "))
 
math_and_calculation(number1, number2)



