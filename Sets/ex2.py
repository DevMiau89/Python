#5. Write a Python program to remove an item from a set if it is present in the set.
num_set = set([0, 1, 2, 3, 4, 5])

z = num_set.discard(6)

print z


#6. Write a Python program to create an intersection and union of sets. 

s = set([0, 1, 2, 3, 4, 5])
v = set([0, 1, 2, 8, 9, 10])

print "--------------------"
print s.intersection(v)

print s.union(v)

#8. Write a Python program to create set difference.
x = {"a","b","c","d","e"}
y = {"b","c"}

print x.difference(y)



