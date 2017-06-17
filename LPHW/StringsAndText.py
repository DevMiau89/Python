x = "There are %d types of people." % 10

binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not) # 1st place

print x
print y 

print "I said %r." % x # 2nd place
print "I also said : '%s'" % y # 3rd place

hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e