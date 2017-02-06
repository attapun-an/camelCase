camelCase = "ThisIsACameCaseString"
stringLength = len(camelCase)
array = []
for i in range (0,9):
    array.append("None")

print(array)

arrayCounter = 0

#find first cap
for i in range (0,stringLength):
    if camelCase[i].isupper():
        sliceInit = i
        break

for i in range (sliceInit,stringLength):
    if camelCase[i].isupper() or i == stringLength:
        sliceEnd = i
        array[arrayCounter] = camelCase[sliceInit:sliceEnd]
        sliceInit = sliceEnd
        arrayCounter += 1

        print(array)


