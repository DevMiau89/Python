#31. Write a Python program to get the key, value and item in a dictionary. 
d = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

print "key",'   ',"value",'   ',"item"
for k,v in d.items():
    print d.get(k),'   ',k,'   ',k,v
   

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}  
print("key  value  count")  
for count, (key, value) in enumerate(dict_num.items()):
    print(key,"   ",value,'    ', count)  


#32. Write a Python program to print a dictionary line by lines 
my_dict = {'Aex':{'class':'V',  
        'rolld_id':2},  
        'Puja':{'class':'V',  
        'roll_id':3}}  


for i in my_dict:
    print i
    for j in my_dict[i]:
        print (j,':',my_dict[i][j])

