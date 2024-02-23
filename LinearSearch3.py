myList = [85,24,63,45,17,31,96,18]

def linearSearch(listIn, key):
    for index in range(len(listIn)):
        if listIn[index] == key:
            return index
    return -1

print(linearSearch(myList,17))