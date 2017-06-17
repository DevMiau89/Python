#ex30 Write a Python program to print the following floating numbers upto 2 decimal places
#ex31 Write a Python program to print the following floating numbers upto 2 decimal places with a sign
#ex32 Write a Python program to print the following floating numbers with no decimal places
#ex33 Write a Python program to print the following integers with zeros on the left of specified width
#ex34 Write a Python program to print the following integers with '*' on the right of specified width.
#ex35 Write a Python program to display a number with a comma separator
#ex36 Write a Python program to format a number with a percentage.
#ex37 Write a Python program to display a number in left, right and center aligned of width 10

x = 3.1415926  
y = -12.9999 

print "x is rounded up to two places %.2f" % x
print "y is rounded up to two places %.2f" % y

print "x is rounded up to two places %.0f" % x
print "y is rounded up to two places %.0f" % y

z = 6
d = 5

print "z is rounded up to two places {:0>2}".format(z)
print "d is rounded up to two places {:0>3}".format(d)

print "z is rounded up to two places {:*<2}".format(z)
print "d is rounded up to two places {:*^10}".format(d)

x = 684028576
print "printing a number with separators {:,}".format(x)

#ex36 Write a Python program to format a number with a percentage3
total = 0.25

print "Correct answer is: {:.0%}".format(total)

#ex37 Write a Python program to display a number in left, right and center aligned of width 10

j = 10
print "Text is aligned to the left {:<10}".format(j)
print "Text is aligned to the right{:>10}".format(j)
print "Text is centered {:*^10}".format(j)