#57. Write a Python program to check if all items of a list is equal to a given string.

color1 = ["green", "orange", "black", "white"]  
color2 = ["green", "green", "green", "green"] 

print cmp(color1, color2)

print all(color1)
print all(color2)

new_color1 = ["green", "orange", "black", "white"]  
new_string = ' '.join(map(str, new_color1))

print new_string

#58. Write a Python program to replace the last element in a list with another list. 

a_list  = [1, 3, 5, 7, 9, 2, 4, 6, 8]
a_list1 = [1,2,2]

a_list.insert(8, a_list1)
a_list.remove(8)

print a_list

str1 = str(a_list)
str2 = str(a_list1)

z = str1.replace("8", str2)
print z

a_list[-1] = a_list1
print a_list


#59. Write a Python program to check if the n-th element exists in a given list. 

def check_elem(lst1, e):
  for i in lst1:
    if e in lst1:
      print True
    else:
      print False

print check_elem([1, 3, 5, 7, 9, 2, 4, 6, 8], 7)        

