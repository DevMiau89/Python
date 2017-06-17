#41. Write a Python program to remove everything except alphanumeric characters from a string.
import re

text1 = '**//Python Exercises// - 12. '

pattern = re.sub('[^\w]+', '', text1)

print pattern

print "------------------"

#42. Write a Python program to find urls in a string.

text2 = '<p>Contents :</p><a href="http://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'

print re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',text2)

