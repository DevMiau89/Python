def odd_index_remove(str1):
    str2 =str1[0::2]
    return str2
    
         

print odd_index_remove('dupa')  

def word_count(str):  
    counts = dict()
    words = str.split()  
  
    for word in words:  
        if word in counts:  
            counts[word] += 1  
        else:  
            counts[word] = 1  
  
    return counts  



print (word_count("kot is kot firend"))

def word_count_occurances(str1):   
    words = str1.split()

    for word in words:
        if word in words > 1:
            return word  +  ' = '  + str(1)
        else:
            return word + str(1)    
    return words
  

print (word_count_occurances("this is cat"))
