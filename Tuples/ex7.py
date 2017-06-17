# 17. Write a Python program to unzip a list of tuples into individual lists
l = [(1,2), (3,4), (8,9)] 

w = zip(*l)

print w

#18. Write a Python program to reverse a tuple.

m = (1,2), (3,4), (8,9)

new_tup = sorted(m, reverse = True)
print "--------------------"
print new_tup

tup = tuple(reversed(m))
print "--------------------"
print tup

z = m[::-1]
print z