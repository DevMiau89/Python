

entry_list = ["red", "white", "black", "red", "green", "black"]

def unique_words(word_list):
    output_list = []
    for word in word_list:
        if word not in output_list:
            output_list.append(word)
    return output_list

print(unique_words(entry_list))