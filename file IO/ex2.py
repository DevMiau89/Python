#2. Write a Python program to read first n lines of a file.
def read_lines(file_name, n):
    file = open(file_name)
    answer = ''
    for i in range(n):
        answer += (file.readline())
    return answer
    file.close()
    

print read_lines("C:\case_test.txt", 1)    
