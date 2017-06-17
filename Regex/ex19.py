#23. Write a Python program to replace whitespaces with an underscore and vice versa. 
import re

text = 'Python Exercises'
text =text.replace (" ", "_")
print(text)
text =text.replace ("_", " ")
print(text)

#24. Write a Python program to extract year, month and date from a an url.

url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
pattern = r'[a-z\:\/\-\.]+(\d+)\/(\d+)\/(\d+)'


match = re.match(pattern, url1)

print match

print match.group(0)
print "------------"
print match.group(1)
print "------------"
print match.group(2)
print "------------"
print match.group(3)



match = re.finditer(pattern, url1)

print "------------"

date = []
for i in match:
    date.append(i.group())

print date
