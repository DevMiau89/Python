#19. Write a Python program to convert a list of tuples into a dictionary.
tup = (1,2), (3,4), (8,9)

d = dict((k,v) for k,v in tup)

print d

#20. Write a Python program to print a tuple with string formatting. 

Sample_tuple = (100, 200, 300)

print "This is a tuple {0}".format(Sample_tuple)

#21. Write a Python program to replace last value of tuples in a list.

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

new_tup = [t[::2] + (100,) for t in l]

print "----------------------"
print new_tup

for t in l:
    print t[:2] + (100,)

   



