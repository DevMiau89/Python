#1. Write a Python program for binary search.
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)/2
        print midpoint
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                print a_list[midpoint]
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
    print a_list[midpoint]

print binary_search([1,2,3,5], 6)

