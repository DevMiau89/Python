from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    print f.seek(1,2)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "\nFirst let's print the whole file:\n"
print_all(current_file)

print "\nNow let's rewind, kind of like a tape."

rewind(current_file)

print "\nLet's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line(current_line, current_file) 

# Mistakes -> I put space beween last letter of the function and "("      
# I didn't put zero in seek funtion!