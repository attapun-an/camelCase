array = []
for i in range(10):
    array.append("")

ccStr = "ThisIsACamelCaseString"

arrI = -1
firstFound = False

#Loop through each letter in the string
for letter in ccStr:
    if letter.isupper():
        arrI += 1
    #If the letter is an uppercase letter
    array[arrI] += letter


print(array)

# Goes through the code and for every capital letter increases the array index
