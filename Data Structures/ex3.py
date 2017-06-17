#3. Write a Python program to display all the member name of an enum class ordered by their values.
from enum import Enum  
class Country(Enum):
    Afghanistan = 93  
    Albania = 355  
    Algeria = 213  
    Andorra = 376  
    Angola = 244  
    Antarctica = 672

z = [c.name for c in Country] 

d = sorted(z)

print d

#4. Write a Python program to get all values from an enum class.

v = [c.value for c in Country]

print v