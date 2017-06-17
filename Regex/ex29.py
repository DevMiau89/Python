#43. Write a Python program to split a string at uppercase letters
import re

text1 = "PythonExercisesAndO"

pattern = re.findall('[A-Z][a-z]*', text1)

print pattern
print "------------------------"

#44. Write a Python program to do a case-insensitive string replacement. 
text2 = "Hello WOrld"

search = re.search(r"WORLD", text2, flags= re.I)

print search.group()
print "------------------------"

#45. Write a Python program to remove the ANSI escape sequences from a string.

text3 = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"

new_text = re.sub('\W+','', text3)

print new_text
