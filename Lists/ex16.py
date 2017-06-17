#63. Write a Python program to insert a given string at the beginning of all items in a list.
sample_list = [1,2,3,4]


new_list = []
for i in sample_list:
    str1 = "emp" 
    str_i = str(i)
    new_list.append(str1 + str_i)
print new_list

num = [1,2,3,4]  
print(['emp{0}'.format(i) for i in  num])

#64. Write a Python program to iterate over two lists simultaneously.
import itertools

lst1 = [1,2,3,4]
lst2 = [5,6,7,8]


for (i,j) in zip(lst1,lst2):
    print i,j


def custom_zip(seq1, seq2):
    it1 = iter(seq1)
    it2 = iter(seq2)
    while True:
        yield next(it1), next(it2)

x = custom_zip(1,2)
print x


#65. Write a Python program to access dictionary keys element by index.
num = {'physics': 80, 'math': 90, 'chemistry': 86}  

print(list(num)[0]) 

#66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.

Sample_lists = [1,2,3], [4,5,6], [10,11,12], [7,8,9]

print max(Sample_lists, key=sum)