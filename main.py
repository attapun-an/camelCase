camelCase = "ThisIsACameCaseString"
length = len(camelCase)
array = []
for i in range (0,9):
    array.append("None")

print(array)

#find start letter:
for i in range (0, length):
    if camelCase[i].isupper():
        startIndex = i
        break

arrayCounter = 0



for i in range (startIndex, length):
    if camelCase[i].isupper:
        startIndex = i
        for i in range(startIndex, length):
            if camelCase[i].isupper:
                sliceIndex = i
                array[arrayCounter] = camelCase[startIndex:sliceIndex]
                arrayCounter += 1
                print(array)
                startIndex = sliceIndex
