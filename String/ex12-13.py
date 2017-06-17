#ex12
name = raw_input('>>> Please enter your name:')

str1 = name.upper()
str2 = name.lower()

print "Here are is your name %s and another one %s" % (str1,str2)

#ex13
words = raw_input('>Please enter the words and seprate them by comma: ')

word = words.split(',')

sorted_word = word.sort()

print word

#ex14
def html_string(str1, str2):
    