#19
def string_first_half(str1):
    if len(str1) % 2 == 0:
        return str1[0:3]
        

print string_first_half('Python')

#ex20
def multiple4_reverse(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]

print multiple4_reverse('kocikoci')        

#ex21
def convert_string(str1):
    if str1[0:2].isupper() or str1[2:4].isupper():
        new_string = str1.upper()
        return new_string
    else:
        return str1  
        

print convert_string('koto')  

def to_uppercase(str1):  #
    num_upper = 0  #counter variable with 0 value
    for letter in str1[:4]: # looping up to 4th letter in str1 
        if letter.upper() == letter: #checking if the letter is upper 
            num_upper += 1 # adding one to the counter variable if up to  4th letter, the l;etter is upper 
    if num_upper >= 2:  #checking if in the string there are already two upper characters
        return str1.upper() #returning upper string has two upper characters
    return str1  #returning string
  
print(to_uppercase('Python')) #calling function 
print(to_uppercase('PyThon')) #calling function    

#ex22 -> Write a Python program to sort a string lexicographically
def string_sort(word):
    sorted_word = sorted(word)
    return sorted_word

print string_sort('puch')    

#ex23 -> Write a Python program to remove a newline in Python
def newline_remove(sentence):
    new_sen = sentence.replace('\n', '')
    return new_sen    

print newline_remove('this is\n new line\n and anothen\n new line')

#rstrip function removes what we have at the end of the string
str1 = 'This is a cat\n'
print str1.rstrip('\n')



    