def longest_word(str1, str2, str3):
    lenght1 = len(str1)
    lenght2 = len(str2)
    lenght3 = len(str3)
    
    if lenght1 > lenght2 and lenght3:
        return lenght1
    elif lenght2 > lenght1 and lenght3:
        return lenght2
    else:
        lenght3 > lenght1 and lenght2        
        return lenght3


print longest_word('kot', 'puszyk', 'mich'')    

def find_longest_word(words_list):  
    word_len = []  
    for n in words_list:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return word_len[-1][0] 

print(find_longest_word(["PHP", "Exercises", "Backend"]))   

#ex10
def remove_char(str, n):  
    first_part = str[:n]   
    last_pasrt = str[n+1:]  
    return first_part + last_pasrt

print(remove_char('Python', 0))  
print(remove_char('Python', 3))  
print(remove_char('Python', 5))  
