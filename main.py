camelCase = "ThisIsACamelCaseString"
# camelCase = input("Input camel case: ")
stringLength = len(camelCase)
print(stringLength)
array = []


for i in range (0,10):
    array.append("None")

arrayCounter = 0

#find first cap
for i in range (0,stringLength+1):
    if camelCase[i].isupper():
        # to ensure the first letter is not included
        sliceInit = i
        break

for i in range (sliceInit+1,stringLength):
    if camelCase[i].isupper():
        sliceEnd = i
        array[arrayCounter] = camelCase[sliceInit:sliceEnd]
        sliceInit = sliceEnd
        arrayCounter += 1

    elif i == stringLength-1:
        sliceEnd = i+1
        array[arrayCounter] = camelCase[sliceInit:sliceEnd]

print(array)


# Task 3.5 Formatting
newArray = []

for i in range (0,10):
    if array[i] != "None":
        newArray.append(array[i])

print (newArray)

Output = " ".join(newArray)

print(Output)









