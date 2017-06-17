cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/ cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars"
print "We can transoprt", carpool_capacity, "people today."
print "We have", passengers, "to carpoll today"
print "We need to put about", average_passengers_per_car, "in each car."

#Python Calculator 

i = 12
j = 6
x = 2

result_1 = i + x
result_2 = i - j
result_3 = i / j
result_4 = x**2
result_5 = i % 5
result_6 = 20.0 // 6.0

print "\nResult% of addition is :", result_1  #Addition
print "\nResult of subtraction is :",result_2 #Subtraction
print "\nResult of division is :",result_3   #Division
print "\nResult of Multiplication is :",result_4  #Multiplication
print "\nResult of modulus is :",result_5   #Modulus
print "\nResult of division is :",result_6   #Division
print "Hey %s there", print "% you".
