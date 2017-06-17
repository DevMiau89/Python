#33. Write a Python program to check multiple keys exists in a dictionary.
student = {
  'name': 'Alex',
  'class': 'V',
  'roll_id': '2'
}

for key in student.keys():
    if key == 'name':
        print True
    elif key == 'class':
        print True
    elif key == 'roll_id':
        print True        
    else:
        print False


print "--------------------"

foo = {'foo': 1, 'zip': 2, 'zam': 3, 'bar': 4}

if set(('class', 'name')).issubset(student):
    print "TRUE"


#34. Write a Python program to count number of items in a dictionary value that is a list.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 

count = 0
for v in num.values():
    count +=1

print count  
print '----------------'

for j in num.keys():
    z = num[j][0] + num[j][1] + num[j][2]
    print z




    