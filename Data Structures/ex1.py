#1. Write a Python program to create an Enum object and display a member name and value.
x = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antarctica"]
y = ["93", "355", "213", "376", "244", "672"]

for name,value in enumerate(zip(x,y)):
    print name, "Member name:" + value[0] + "\n " + "Member value = " + value[1]

print "--------------------------"

from enum import Enum  
class Country(Enum):
    Afghanistan = 93  
    Albania = 355  
    Algeria = 213  
    Andorra = 376  
    Angola = 244  
    Antarctica = 672

print('\nMember name: {}'.format(Country.Albania.name))  
print('Member value: {}'.format(Country.Albania.value))  