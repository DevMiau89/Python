moj_string = 'misiomis'
pierwsza_litera = moj_string[0]

if pierwsza_litera in moj_string[1:]:
    one = moj_string.replace(pierwsza_litera,"$")

    print pierwsza_litera + one[1:]
        
def change_char(str1):
     char = str1[0]  
     #length = len(str1)  
     str1 = str1.replace(char, '$')  
     str1 = char + str1[1:]
     
     return str1  
  
print(change_char('restart'))   