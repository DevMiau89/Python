def right_justify(s):
    print "%70s" % s


right_justify('allen')


def do_twice(f, val):
    f(val)
    f(val)

def print_twice(printVal):
    print printVal

val = 'spam'

do_twice(print_twice, val)

# Part Two
def do_twice(f, val):
    f(val)
    f(val)

def print_twice(printVal):
    print printVal

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

val = 'spam'

do_four(print_twice, val)         

# I modified do_twice() and do_four()

def do_Func(f, val, iter):
    i=0 
    while i < iter:
        f(val)
        i=i+1

def printer(val):
    print val

# Create Grid

colCell = '+ - - - - + - - - - +'
rowCell = '|         |         |'

do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)