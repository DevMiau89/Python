#ex1 Write a Python program to sum all the items in a list.

def sum_list(items):  
    sum_numbers = 0  
    for x in items:  
        sum_numbers += x  
    return sum_numbers  

print(sum_list([1,2,-8]))      

#ex2 Write a Python program to multiplies all the items in a list. 


def sum_list(items):  
    sum_numbers = 1  
    for x in items:  
        sum_numbers *= x  
    return sum_numbers  

print(sum_list([2,-8]))   

#ex3 Write a Python program to get the largest and smallest number from a list.

a_list = [123, 5, 21, 89]

print "Max value element : {0}".format(max(a_list))

print "Min value element : {0}".format(min(a_list))

#ex5 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.


def match_words(words):  
    ctr = 0  
      
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1  
    return ctr  
    
print(match_words(['abc', 'xyz', 'aba', '1221']))  

#ex6 Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

t = [1, 2, 3]
print sum(t)



sorted_list = ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])    

new_items = sorted(sorted_list)
print new_items


