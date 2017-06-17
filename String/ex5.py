s = ' '
sample_string = ('abc','xyz')

join_string = s.join(sample_string)

new_string = join_string.replace("xy","ab")

print join_string[4:6] + new_string[2:]

def chars_mix_up(a, b):  
    new_a = b[:2] + a[2:]  
    new_b = a[:2] + b[2:]  
      
    return new_a + ' ' + new_b  
print(chars_mix_up('abc', 'xyz'))  


def chars_mix_up(a, b):  
    return b[:2] + a[2:]  + ' ' + a[:2] + b[2:]
print(chars_mix_up('abc', 'xyz'))  