def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just finctions!"

age = add(int(raw_input()),int(raw_input()))
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2) 

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))  
print "That becomes:", what, "Can you do it by hand?"

print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'