def change_char(str1):
    ending = 'ing' 
    if len(str1) > 3 and str1[-3:] != ending:
         str1.replace('ing', 'ly')
    else:
        str1 += 'ing'
    return str1

    

print change_char('kot')  