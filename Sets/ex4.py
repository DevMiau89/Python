#12. Write a Python program to clear a set. 
x = {"a","b","c","d","e"}

z = x.clear()

print z

#13. Write a Python program to use of frozensets.
y = {"a","b","c","d","e"}

fset = frozenset(y)

print fset

#14. Write a Python program to find maximum, lenght and the minimum value in a set. 
num_set = set([0, 1, 2, 3, 4, 5])

print max(num_set)
print min(num_set)
print len(num_set)