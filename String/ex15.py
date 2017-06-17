def add_html_taggs(tag, str1):
    new_tag = '<{0}>{1}</{0}>'.format(tag, str1)
    return new_tag

print add_html_taggs('i', 'python')    


def test_html_taggs():
    assert add_html_taggs('i', 'python') == '<i>python</i>'