def insert_string_middle(tag, str1):
    new_tag = tag[0:2] + str1 + tag[2:5]
    return new_tag

print insert_string_middle('{{}}', 'PHP')  


def test_string_middle():
    assert insert_string_middle('{{}}', 'PHP') == {{PHP}}
