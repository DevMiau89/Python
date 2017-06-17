#3. Write a Python program that matches a string that has an a followed by one or more b's
import re
def text_match(string):
    pattern = 'b+a'
    p = re.match(pattern, string)
    if p:
        print True
    else:
        print False

text_match("ddd")

print '---------------------'

#4. Write a Python program that matches a string that has an a followed by zero or one 'b'.

def search_text(str1):
    p = re.match(r'b?a', str1)
    if p:
        print "Match found"
    else:
        print "No results"

search_text("c")
