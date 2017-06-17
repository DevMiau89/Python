#10. Write a Python program to check whether an element exists within a tuple.
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7 

print 2 in tuplex
print 7 in tuplex

def check_element(seq, elem):
    if elem not in seq:
        return "Element does not exist" 
    else: 
        return "Element exists"  


print check_element((2, 4, 5, 6, 2, 3, 4, 4, 7) , 100)       


#11. Write a Python program to convert a list to a tuple.
sample_list = ['abc', 'xyz', 'aba', 'abc']

my_tup = tuple(sample_list)

print my_tup

#12. Write a Python program to remove an item from a tuple.
tup = ('abc', 'xyz', 'aba', 'abc')

my_list = list(tup)

my_list.pop(0)

print my_list

tup = tup[1:2] + tup[2:3]

print "-------------------"
print tup