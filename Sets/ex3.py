x = {"a","b","c","d","e"}
y = {"b","c"}

x.difference_update(y)

print x

#9. Write a Python program to create a symmetric difference.
s = set("ABC")
t = frozenset('bookBC')

print s ^ t

#10. Write a Python program to issubset and issuperset. 
num_set = set([0, 1, 2, 3, 4, 5])
v = set([0, 1, 2, 8, 9, 10])

print "-----------------"
print num_set.issubset(v)
print num_set.issuperset(v)

#11. Write a Python program to create a shallow copy of sets. 
my_set = set([0, 1, 2, 3, 4, 5])
my_set.add(7)

set_copy = my_set.copy()

set_copy.add(6)

print my_set
print set_copy
