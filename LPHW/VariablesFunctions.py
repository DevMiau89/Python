#this one is like scripts with argv
def print_two(*args):
    arg1,arg2= args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#simpler way
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1 : %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothing"

print_two ("Karolina", "Puszyk")
print_two_again ("Karolina","Kocha Puszyk")
print_one("Puszyk")
print_none()


# Mistake -> I didn't add at the end ':'

#What does *arg mean -> That tells Python to take all the arguments to the function and then put them in args as a list.
def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

test_var_args(1, "two", 3)


# function checklist
def checklist(arg1, arg2):
    print "This is a checklist function with two arguments : %r and %r" % (arg1,arg2)

checklist('Kot', 'Puszyk')    
