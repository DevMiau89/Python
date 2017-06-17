#3. Write a Python program for binary search for an ordered list.
def ordered_binary_search(a_list, item):
    a_list.sort()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)/2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                print a_list[midpoint]
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, midpoint
print ordered_binary_search([5,6,7,1,7,2,4], 2)