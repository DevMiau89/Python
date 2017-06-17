def first_three(str1):
    if len(str1) > 3:
        return str1[0:3]
    else:
        return str1

print first_three('karolina')            

def insert_end(str2):
    if len(str2) > 2:
        new_str2 = str2[0:2] * 4
        return new_str2
  
#ex18

print insert_end('koci')            

def test_first_three():
    assert first_three('karolina') == 'kar'

def test_insert_end():
    assert insert_end('koci') == 'kokokoko'    