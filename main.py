camelCase = "ThisIsACameCaseString"
stringLength = len(camelCase)
array = []
for i in range (0,9):
    array.append("None")

print(array)


sliceInit = 0
arrayCounter = 0
sliceEnd = 0


while sliceEnd <= stringLength:
    if camelCase[sliceEnd].isupper():
        sliceInit = sliceEnd

        print(sliceEnd)
        print(stringLength)
        for i in range (sliceEnd, stringLength):
            if camelCase[sliceEnd].isupper() or sliceEnd >= stringLength:
                print("meow")
                print(camelCase[sliceInit:sliceEnd])
                array[arrayCounter] = camelCase[sliceInit:sliceEnd]
                arrayCounter += 1
                sliceInit = sliceEnd
                break


    else:
        sliceEnd += 1




