#1. Write a Python program to create a set.

s = {2.2, "kot", 2, "mich", 3}

new_set = set()

m = set([1,2])

print new_set
print s
print m

#2. Write a Python program to iteration over sets.
my_set = set(["Perl", "Python", "Java"])

new_s = [x for x in my_set]

print new_s

num_set = set([0, 1, 2, 3, 4, 5])

for n in num_set:
    print n

#3. Write a Python program to add and remove member(s) in a set 
num_set = set([0, 1, 2, 3, 4, 5])
num_set.add(6)
num_set.update("kot", "puch")
num_set.remove(4)
num_set.pop()

print num_set