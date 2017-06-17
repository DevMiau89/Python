import sys

print (sys.version)

x = 50
print "width = {0}".format(x)

import textwrap

sample_text = ''' 
  Python is a widely used high-level, general-purpose, interpreted, 
  dynamic programming language. Its design philosophy emphasizes 
  code readability, and its syntax allows programmers to express 
  concepts in fewer lines of code than possible in languages such 
  as C++ or Java. 
  '''
print()
print(textwrap.fill(sample_text,width=50))
print()  

text_without_indentation = textwrap.dedent(sample_text)
print text_without_indentation


#ex 27 Write a Python program to remove existing indentation from all of the lines in a given text.

sample_string = ''' 
  Python is a widely used high-level, general-purpose, interpreted, 
  dynamic programming language. Its design philosophy emphasizes 
  code readability, and its syntax allows programmers to express 
  concepts in fewer lines of code than possible in languages such 
  as C++ or Java. 
  '''

print sample_string.replace("\t", "")


sample_string1 = "8 Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.888888"
print sample_string1.rstrip('8')

#ex28 and ex29 Write a Python program to add a prefix text to all of the lines in a string/  Write a Python program to set the indentation of the first line.
from textwrap import*  
sample_text =''' 
    Python is a widely used high-level, general-purpose, interpreted, 
    dynamic programming language. Its design philosophy emphasizes 
    code readability, and its syntax allows programmers to express 
    concepts in fewer lines of code than possible in languages such 
    as C++ or Java. 
    '''  
text_without_Indentation = textwrap.dedent(sample_text)  
wrapped = textwrap.fill(text_without_Indentation, width=50)  
#wrapped += '\n\nSecond paragraph after a blank line.'  
final_result = textwrap.fill(sample_text,width =50, initial_indent = '>', subsequent_indent = "> ")
print()  
print(final_result)  
print()  

