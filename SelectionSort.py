myList = [85, 24, 63, 45, 17, 31, 96, 50]
for index in range(len(myList)-1):
    print(myList)
    nextMinValue = min(myList[index+1:])
    if nextMinValue < myList[index]:
        nextMinIndex = myList.index(nextMinValue)
        myList[nextMinIndex] = myList[index]
        myList[index] = nextMinValue
print(myList)
print (myList.index(45))