#60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.

x = [(4, 1), (1, 2), (6, 0)] 

z = min(x, key=lambda x: x[1])

print z

#61. Write a Python program to create a list of empty dictionaries.

n = 5

l = [{} for i in range(n)]

print l

new_list = []
for i in range(3):    
    new_list.append({})
    print new_list

#62. Write a Python program to print a list of space-separated elements.

color1 = ["green", "orange", "black", "white"]  

joined_colors = " ".join(color1)

print joined_colors


num = [5, 6, 7, 8]  

print (*num)