my_name = "Puszyk"
my_age = 35
my_height = 173 #centimeters
my_weight = 59 #kilograms
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about {}.".format (my_name)
print "He is {0} centimeters tall.".format(my_height)
print "He's %d kilogams heavy." %my_weight
print "That is not actually too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# tricky line
print "if I add %s, %d, and %d I get %d." % (my_age, my_height,my_weight, my_age + my_height + my_weight)

#Conversion

# int
age = 21

print "You must be {0} years old".format(age)

#  number to string

i = 100
f = 1.3

print str(f)
print str (i)



