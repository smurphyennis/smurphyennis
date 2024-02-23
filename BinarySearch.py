myList = [73, 24, 31, 45, 34,  63, 85, 96, 56]

def binarySearchLoop(listIn, key):
    first = 0
    last = len(listIn)-1
    while (last - first) >= 0:
        middle = first + ((last - first)//2)
        if listIn[middle] == key:
            return middle
        elif key < listIn[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return -1

print(binarySearchLoop(myList, 31))
