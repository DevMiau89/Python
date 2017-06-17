#ex30. Write a Python program to get the frequency of the elements in a list.

from collections import Counter

mylist = [1, 1, 2, 2, -2, -8, -2, 0]

counts = Counter(mylist)

print counts

#31. Write a Python program to count the number of elements in a list within a specified range.

mylist = [1, 1, 2, 2, -2, -8, -2, 0]

counts = Counter(mylist[1:5])

print counts

#32. Write a Python program to check whether a list contains a sublist. 

mylist = [1, 1, 2, 2, -2, -8]
sub_list = [0,0]

se1 = set(mylist)
se2 = set(sub_list)

new_seq = se2.issubset(mylist)

print new_seq

#ex33 Write a Python program to generate all sublists of a list.

def sub_lists(my_list):  #func declaration
    subs = [[]]  # declaring nested list
    for i in range(len(my_list)):  #iteration through the whole list
        n = i+1  #Variable declaration for range
        while n <= len(my_list):  # Keep looping until reach the lenght of the list
            sub = my_list[i:n]  #Assignment to var sub, range from i to n to indicate the sub
            subs.append(sub) # Adding to the sub list 
            n += 1  #Increasing n number
      
    return subs #returning sub list

print sub_lists(['X', 'Y', 'Z']) #function call



from itertools import combinations

def all_slices(s):
    for start, end in combinations(range(len(s)), 2):
        yield s[start:end+1]




print sub_lists([1, 2, 3])


from itertools import permutations
for i in range(3):
    i = i+1
    perm = list(permutations(['X', 'Y', 'Z'],i))
    print perm

