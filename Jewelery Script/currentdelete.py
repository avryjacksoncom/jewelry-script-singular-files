import os
import re 
import time
from collections import Counter



# MXX01X
# RXX01

# 212 singular files
directory = "/Users/avryjackson/Desktop/TestFolder"
file_name = "newsorted.txt"
file_name2 = "test2.txt"
sortedFile = "mysortedfile.txt"
sortedTest = "sortedTest.txt"
psdtxt = "test5psd.txt"
fileTag1 = "UMXXX01X.txt"
fileTag2 = "URXX01.txt"
uneditedList = "Unedited List.txt"
underscore = "underscore.txt"
newFile = "UeditedList.txt"
checkFile = "testteset.txt"
ourfirstTagFile = "testTag.txt"
untagPart1 = "testuntag.txt"
listwithoutunderscores = "testlistwithoutunderscores.txt"


# example = "fjasdjaw copy"

# print(example)
# print(example.rstrip())
# time.sleep(100)

# with open(file_name, 'w') as file:
#     file.write("T")
# print(f"File '{file_name}' created successfully.")



# with open(file_name, "w") as file:
#     for root, dirs, files in os.walk(directory):
#         for i in files:
#             file_name = os.path.join(i.strip())
#             print(i)
#             file.write(file_name)
#             file.write("\n")




# number we ned to get is 2388

arrayNames = []
psdNames = []
mxx = []
rxx = []

# with open(sortedFile, "r") as file:
#     for line in file:
#         if ".psd" in line:
#             print(line)
#             psdNames.append(line)
#         else:
#             # lineNames = line.split("-",1)
#             print(line)
#             arrayNames.append(line)

# with open(uneditedList, "r") as file:
#     for line in file:
#         if "MXX01X" in line:
#             print(line)
#             mxx.append(line)

# with open(uneditedList, "r") as file:
#     for line in file:
#         if "RXX01" in line:
#             print(line)
#             rxx.append(line)

# with open(fileTag1,"w") as file:
#     for i in mxx:
#         file.write(i)


# with open(fileTag2,"w") as file:
#     for i in rxx:
#         file.write(i)

filenewArr = []
# with open(sortedFile, "r") as file:
#     for line in file:
#         if "_" in line and ".psd" not in line:
#             print(line)
#             mxxNew.append(line)

newFile = []
tempArr = []
count = 0
prevLine =""
newStr = ""
tempCount = 0
iteratorCount = 0
checkArr = []
arrC = []

with open(file_name,"r") as file:
    for line in file:
        arrC.append(line.lower())

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
                break
            if char == ".":
                break
            if char == " ":
                break
            try:
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
 
        print(f"this is the temp string {tempstring}")
        print("\n")
        if tempstring == "":
            continue
        else:
            indexArr += 1
            arrCheck.append(tempstring)
            
        if count == 0:
            print("where at the first count")
            pass
        else:
            pass
             
        count += 1
        arrayCharCheck = []
        originalString.append(word)
        tupleString.append([word,tempstring])

print("arrayCheck3 below")
print(len(arrCheck))
for word in arrCheck:
    print(word)

print(len(arrCheck))

# with open(listwithoutunderscores,"w") as file:
#     for word in arrCheck:
#         file.write(word + "\n")


for word in tupleString:
    print(f" word 1 = {word[0]} word 2 = {word[1]}")
   
print("\n")

# arrayCheck below
# ['MXXX01-IIII', 'MXXX01-IIII2', 'UURRF', 'UURRF444', 'aaa', 'aaa', 'MXXX01-IIII', 'MXXX01-IIII', 'MXXX01-IIII', 'MFHSADFJ-', 'MFHSADFJ234234-']
lengthOfArray = len(arrCheck) - 1
markerArr = []
firstTag = ""
buildWord = ""
buildCount = 0
firstTagArr = []
arrWithWhiteSpaces = []
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
                # if the prev word, current word
                #        same word, same word
                #        differnt word, different word

                # if arrCheck[index - 1 ] == arrCheck[index]:
                        # if the current word = the first word and the first word does not equal the next word

                        #            pointer
                        # same word, same word, different word
                        # we need to delete if its 

                if arrCheck[index] == arrCheck[index - 1] and arrCheck[index + 1] !=arrCheck[index]:
                    print("\n")
                    print("True1 so we just continue and move index , Same Word, Same Word, Different Word")
                    print("\n")
                    print("-------------------------------------------")
                    continue
                       #                pointer
                # differnt word, current word, different word
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

for i in range(len(tupleString)):
    word = tupleString[i][0].strip()
    if "-" in word:
        temp = word.split("-", 1)[0]
        prefixes.append(temp)
    else:
        prefixes.append(word)

# Now you have prefixes corresponding to each original entry.
print(prefixes)

markerArr = []
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
                # if the prev word, current word
                #        same word, same word
                #        differnt word, different word

                # if arrCheck[index - 1 ] == arrCheck[index]:
                        # if the current word = the first word and the first word does not equal the next word

                        #            pointer
                        # same word, same word, different word
                        # we need to delete if its 

                if prefixes[index] == prefixes[index - 1] and prefixes[index + 1] !=prefixes[index]:
                    print("\n")
                    print("True1 so we just continue and move index , Same Word, Same Word, Different Word")
                    print("\n")
                    print("-------------------------------------------")
                    continue
                       #                pointer
                # differnt word, current word, different word
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



import os

directory = "/Users/avryjackson/Desktop/TestFolder"


# for filename in finalArr:
#     full_path = os.path.join(directory, filename)
#     if os.path.exists(full_path):
#         os.remove(full_path)
#         print(f"Deleted: {full_path}")
#     else:
#         print(f"Not found: {full_path}")
print("end")
time.sleep(10000)