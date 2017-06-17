#8.Write a Python program to get the unique enumeration values.
from enum import Enum,unique

@unique  
class Country(Enum):
    Afghanistan = 93  
    Albania = 355  
    Algeria = 213  
    Andorra = 376  
    Angola = 244  
    Antarctica = 672  

for i in Country:
    print "{} = {}".format(i.name, i.value)
print "----------------------------"

#9. Write a Python program to create an instance of an OrderedDict using a given dictionary. Sort the dictionary during the creation and print the members of the dictionary in reverse order.    
from collections import OrderedDict

ordered_dictionary = OrderedDict()

ordered_dictionary["Angola"] = 44
ordered_dictionary["Andorra"] = 376
ordered_dictionary["Algeria"] = 213
ordered_dictionary["Afghanistan"] = 93
ordered_dictionary["Albania"] = 355

for key in reversed(ordered_dictionary):
    print key, ordered_dictionary[key]

