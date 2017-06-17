#16. Write a Python program to get a dictionary from an object's fields.
class dictObj(object):  
     def __init__(self):  
         self.x = 'red'  
         self.y = 'Yellow'  
         self.z = 'Green'  
       
test = dictObj()  
print(test.__dict__) 

#17. Write a Python program to remove duplicates from Dictionary. 

student_data = {'id1':   
   {'name': ['Sara'],   
    'class': ['V'],   
    'subject_integration': ['english, math, science']  
   },  
 'id2':   
  {'name': ['David'],   
    'class': ['V'],   
    'subject_integration': ['english, math, science']  
   },  
 'id3':   
    {'name': ['Sara'],   
    'class': ['V'],   
    'subject_integration': ['english, math, science']  
   },  
 'id4':   
   {'name': ['Surya'],   
    'class': ['V'],   
    'subject_integration': ['english, math, science']  
   },  
} 

result = {}

for k,v in student_data.items():
    if v not in result.values():
        result[k] = v

print result    
       