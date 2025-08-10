import os
import re 
import time
from collections import Counter

# I defintely can make this more efficient later
# But this script works for finding the singular files
# From seraching form the first two tags then to one tag.
# My Job just needed the singular files gone and brute forcing
# it was the easiest way for me to do it.

file_name = "newsorted.txt"
filenewArr = []

arrC = []
# original file of the jewelry folder
with open(file_name,"r") as file:
    for line in file:
        arrC.append(line.lower())

# Just fair warning I honestly probably have too many variables in the file.
# I was testing a lot for this script.

print(arrC)
tempstring = ""
firstTag = ""
count = 0
arrCheck = []
indexArr = 0
tempWord = ""
arrayCharCheck = []
originalString =[]
tupleString = []
for word in arrC:

        tempstring = ""
        charCount = 0
        for i in range(len(word)):
          
            char = word[i]
            # we skip word
            if ".psd" in word:
                # basically were gunna save all these files somewhere else
                # since there not actual hosted files and they are photoshop files.
                break
            if char == ".":
                break
            if char == " ":
                break
            try:
                # building array to check patterns.
                if char == "_":
                    arrayCharCheck.append("_")
                if char == "-":
                    arrayCharCheck.append("-")
                    print("this is the char count")
                    print(charCount)
                    charCount += 1

                    if word[i + 1] is None:
                        tempstring = word 
                        print(word)
                if charCount == 2:
                    break

                elif arrayCharCheck is None:
                     pass
                
                elif len(arrayCharCheck) == 2:
                    if arrayCharCheck[0] == "-" and arrayCharCheck[1] == "_":
                        arrayCharCheck = []
                        break
                    elif arrayCharCheck[0] == "_" and arrayCharCheck[1] == "_":
                        arrayCharCheck = []
                        break
                    elif arrayCharCheck[0] == "_" and arrayCharCheck[1] == "-":
                        arrayCharCheck = []
                        break

            except IndexError:
                print("Index error")

            tempstring += char
 
        print(f"This is the temp string {tempstring}")
        print("\n")
        if tempstring == "":
            continue
        else:
            indexArr += 1
            arrCheck.append(tempstring)
            
        if count == 0:
            print("Where at the first count")
            pass
        else:
            pass
             
        count += 1
        arrayCharCheck = []
        originalString.append(word)
        # appending the edited string and the original filename
        # in order to keep tract which index and name for later use.
        tupleString.append([word,tempstring])

print("arrayCheck3 below")
print(len(arrCheck))
for word in arrCheck:
    print(word)

print(len(arrCheck))

for word in tupleString:
    print(f" word 1 = {word[0]} word 2 = {word[1]}")
   
print("\n")

# The comment below is just Testing for the pointer logic
# ['MXXX01-IIII', 'MXXX01-IIII2', 'UURRF', 'UURRF444', 'aaa', 'aaa', 'MXXX01-IIII', 'MXXX01-IIII', 'MXXX01-IIII', 'MFHSADFJ-', 'MFHSADFJ234234-']
lengthOfArray = len(arrCheck) - 1
markerArr = []
firstTag = ""
buildWord = ""
buildCount = 0
firstTagArr = []
arrWithWhiteSpaces = []

# Checks the postions of the current word.
# Marks the index at where there is a singular file.
for index in range(len(arrCheck)):

        if index == 0:
            print("we are at the first word")
            print(arrCheck[index])
            print("\n")
            if arrCheck[index] != arrCheck[index + 1]:
                markerArr.append(index)
            pass
        else:
            try:
                # we just simply break here doesnt do anything
                num = arrCheck[index + 1]
                # print(arrCheck)
                print("\n")

                print(f"this is our current pointer {index}")
                print(f" first word: {arrCheck[index - 1]} : {index - 1} | current word: {arrCheck[index]} : {index} \n third word: {arrCheck[index + 1]} : {index + 1}")
                print("\n")
      
                # if arrCheck[index - 1 ] == arrCheck[index]:
                        # if the current word = the first word and the first word does not equal the next word

               
                    #            pointer
                    # same word, same word, different word
                    # we need to keep the current pointer
                if arrCheck[index] == arrCheck[index - 1] and arrCheck[index + 1] !=arrCheck[index]:
                    print("\n")
                    print("True1 so we just continue and move index , Same Word, Same Word, Different Word")
                    print("\n")
                    print("-------------------------------------------")
                    continue
                    #                pointer
                    # differnt word, current word, different word
                    # we need to deltete the current pointer since the other positions of the words are differnt.
                elif arrCheck[index] != arrCheck[index - 1] and arrCheck[index] != arrCheck[index+1]:
                    print("False so we delete the current pointer value.")
                    print(f"Current Value = {arrCheck[index]}")
                    print(f"This is the Index marked and put in arr: {index}")
                    markerArr.append(index)
                    print("-------------------------------------------")
                else:
                    print("-------------------------------------------")
                    pass

            except IndexError:
                print("\n")
                print("at the end of the array")
                print(f" first word: {arrCheck[index - 1]} : {index - 1} | second word: {arrCheck[index]}")
                if arrCheck[index] == arrCheck[index - 1]:
                    print("True")
                else:
                    print("False")
                    print(f"This is the Index marked and put in arr: {index}")
                    markerArr.append(index)
                break

# Step 1: get all base names

print("\n")
print("Here is the marked values in the index below")
print(markerArr)
print("looping though to see the words")
print(len(markerArr))

for i in range(len(markerArr)):
    print(tupleString[i])
    # we just delete the arrcheck[i] here since its marked


prefixes = []
# we are making another array with only the first prefix here instead
# of splitting by two above.
for i in range(len(tupleString)):
    word = tupleString[i][0].strip()
    if "-" in word:
        temp = word.split("-", 1)[0]
        prefixes.append(temp)
    else:
        prefixes.append(word)

# now we have prefixes corresponding to each original entry.
print(prefixes)
markerArr = []

# same exact method as above we just go through one more time and check the first tag only since there
# was still duplicates. 

# Checks the postions of the current word.
# Marks the index at where there is a singular file.
for index in range(len(prefixes)):

        if index == 0:
            print("we are at the first word")
            print(prefixes[index])
            print("\n")
            if prefixes[index] != prefixes[index + 1]:
                markerArr.append(index)
            pass
        else:
            try:
                # we just simply break here doesnt do anything
                num = prefixes[index + 1]
                # print(arrCheck)
                print("\n")

                print(f"this is our current pointer {index}")
                print(f" first word: {prefixes[index - 1]} : {index - 1} | current word: {prefixes[index]} : {index} \n third word: {prefixes[index + 1]} : {index + 1}")
                print("\n")
             

                if prefixes[index] == prefixes[index - 1] and prefixes[index + 1] !=prefixes[index]:
                    print("\n")
                    print("True1 so we just continue and move index , Same Word, Same Word, Different Word")
                    print("\n")
                    print("-------------------------------------------")
                    continue
                #                pointer
                # differnt word, current word, different word
                # we need to deltete the current pointer since the other positions of the words are differnt.
                elif prefixes[index] != prefixes[index - 1] and prefixes[index] != prefixes[index+1]:
                    print("False so we delete the current pointer value.")
                    print(f"Current Value = {prefixes[index]}")
                    print(f"This is the Index marked and put in arr: {index}")
                    markerArr.append(index)
                    print("-------------------------------------------")
                else:
                    print("-------------------------------------------")
                    pass

            except IndexError:
                print("\n")
                print("at the end of the array")
                print(f" first word: {prefixes[index - 1]} : {index - 1} | second word: {prefixes[index]}")
                if prefixes[index] == prefixes[index - 1]:
                    print("True")
                else:
                    print("False")
                    print(f"This is the Index marked and put in arr: {index}")
                    markerArr.append(index)
                break


for i in range(len(markerArr)):
    val = markerArr[i]
    print(val)
    print(arrCheck[val])


print(len(markerArr))

finalArr = []
count = 0
# cleaning up array for deletion
tupleString = [(x[0].strip(), x[1]) for x in tupleString]
for i in range (len(markerArr)):
    val = markerArr[i]
    print(tupleString[val])
    finalArr.append(tupleString[val][0])
    count+= 1

for index in finalArr:
    print(index)

print(len(arrCheck))
print(count)

directory = ""

# Finally Deleting All the marked files

# for filename in finalArr:
#     full_path = os.path.join(directory, filename)
#     if os.path.exists(full_path):
#         os.remove(full_path)
#         print(f"Deleted: {full_path}")
#     else:
#         print(f"Not found: {full_path}")

print("end")