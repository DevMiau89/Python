def find_longest_word(words_list):  
    word_len = []  
    for n in words_list:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))   

def find_longest_wordByMis(word_list):
    longest_word = ""
    for word in word_list:
        if(len(word) > len(longest_word)):
            longest_word = word
    return longest_word

print(find_longest_wordByMis(["PHP", "Exercises", "Backend"]))   