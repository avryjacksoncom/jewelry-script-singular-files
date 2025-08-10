import os
import re 
import time


# MXX01X
# RXX01

# 212 singular files
directory = "/Users/avryjackson/Desktop/TestFolder"
file_name = "test.txt"
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
arrayDict = {'-':0,'_':0}
charCount2 = 0

print(f"for loop")
for word in arrC:
        tempstring = ""
        charCount = 0
        for i in range(len(word)):
        
            
            # buildin char and checking char
            # default cases
            char = word[i]
            if ".psd" in word:
                break
            if "copy" in word:
                break
            if "()" in word:
                break
            if char == ".":
                break
            if char == " ":
                break
          

            try:
                # checking how many special cahracters in string
                # appending them
                # making sure that the next letter if its None were at the end.
                if char == "-":
                    arrayDict['-'] += 1
                    print("this is the char count")
                    print(charCount)
                    charCount += 1
                    if word[i + 1] is None:
                        tempstring = word 
                        print(word)

                elif char == "_":

                    arrayDict['_'] += 1
                    print("this is the char count")
                    print(charCount2)
                    charCount2 += 1

                    if word[i + 1] is None:
                        tempstring = word 
                        print(word)
                if charCount2 == 1:
                    break
                if charCount == 2:
                    break
            
            except IndexError:
                print("Index error")

            tempstring += char

        print(f"this is the temp string {tempstring}")
        print("\n")

        if tempstring == "":
            continue
        else:
            valueUnderscore = arrayDict["_"]
            valueDash = arrayDict["-"]


            indexArr += 1
            arrCheck.append(tempstring)
            
            
        # if valueDash == 2:
        #     indexArr += 1
        #     arrCheck.append(tempstring)
        # elif valueDash == 0 and valueUnderscore == 0:

        # elif valueUnderscore == 2:
        
        # elif valueUnderscore == 1 and valueDash == 1:

        count += 1
        arrayDict = {'-':0,'_':0}


print("arrayCheck3 below")
print(len(arrCheck))
print(arrCheck)

time.sleep(1000)

# with open(listwithoutunderscores,"w") as file:
#     for word in arrCheck:
#         file.write(word + "\n")

time.sleep(10000)
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
                    print("True so we just continue and move index , Same Word, Same Word, Different Word")
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

print("\n")
print("Here is the marked values in the index below")
print(markerArr)
print("looping though to see the words")
print(len(markerArr))

newListv = []
counterTy = 0
tempTy = ""
print("start of ty")
print("length of arrcheck")
print(len(arrCheck))
print(arrCheck)
print("end of list2")
for i in range(len(markerArr)):

    for j in range(len(arrCheck)):
     
        tempTy = markerArr[j]
        if tempTy == i:
            print("we are inside the if")
            newListv.append(arrCheck[j])
  

print("here is list")
print(newListv)
with open(untagPart1,"w") as file:
    for line in newListv:
        file.write(line + "\n")

time.sleep(1000)
       

# for index in markerArr:
#     num = index
#     print(arrCheck[num])


# with open(checkFile, "w") as file:
#     for index in markerArr:
#         file.write(arrCheck[index] + "\n")
       

anotherArr = []
with open(checkFile, "r") as file:
    for line in file:
        anotherArr.append(line.strip())

print("start of arr")
print(anotherArr)

ourFirstTagArr = []

strBuild = ""
for index in range(len(anotherArr)):

    for char in anotherArr[index]:
        if char == "-":
            break
        strBuild += char
      
    
    ourFirstTagArr.append(strBuild)
    strBuild = ""


# with open(ourfirstTagFile, "w") as file:
#     for tag in ourFirstTagArr:
#         file.write(tag + "\n")


anotherArrayTag = []
with open(ourfirstTagFile,"r") as file:
    for line in file:
        anotherArrayTag.append(line.strip())


print(anotherArrayTag)
print("end of array")
tagMarkedArr = []
indexCounter = 0

for index in range(len(anotherArrayTag)):

        if index == 0:
            print("we are at the first word")
            print(anotherArrayTag[index])
            print("\n")
            if anotherArrayTag[index] != anotherArrayTag[index + 1]:
                tagMarkedArr.append(index)
            pass
        else:
            try:
                # we just simply break here doesnt do anything
                num = anotherArrayTag[index + 1]
                # print(arrCheck)
                print("\n")

                print(f"this is our current pointer {index}")
                print(f" first word: {anotherArrayTag[index - 1]} : {index - 1} | current word: {anotherArrayTag[index]} : {index} \n third word: {anotherArrayTag[index + 1]} : {index + 1}")
                print("\n")
                # if the prev word, current word
                #        same word, same word
                #        differnt word, different word

                # if arrCheck[index - 1 ] == arrCheck[index]:
                        # if the current word = the first word and the first word does not equal the next word

                        #            pointer
                        # same word, same word, different word
                        # we need to delete if its 

                if anotherArrayTag[index] == anotherArrayTag[index - 1] and anotherArrayTag[index + 1] !=anotherArrayTag[index]:
                    print("\n")
                    print("True so we just continue and move index , Same Word, Same Word, Different Word")
                    print("\n")
                    print("-------------------------------------------")
                    continue
                       #                pointer
                # differnt word, current word, different word
                elif anotherArrayTag[index] != anotherArrayTag[index - 1] and anotherArrayTag[index] != anotherArrayTag[index+1]:
                    print("False so we delete the current pointer value.")
                    print(f"Current Value = {anotherArrayTag[index]}")
                    print(f"This is the Index marked and put in arr: {index}")
                    tagMarkedArr.append(index)
                    print("-------------------------------------------")
                else:
                    print("-------------------------------------------")
                    pass

            except IndexError:
                print("\n")
                print("at the end of the array")
                print(f" first word: {anotherArrayTag[index - 1]} : {index - 1} | second word: {anotherArrayTag[index]}")
                if anotherArrayTag[index] == anotherArrayTag[index - 1]:
                    print("True")
                else:
                    print("False")
                    print(f"This is the Index marked and put in arr: {index}")
                    tagMarkedArr.append(index)
                break

print("\n")
print("Here is the marked TAGGGEDDD values in the index below")
print(tagMarkedArr)
print("looping though to see the words")
print(len(tagMarkedArr))


FINALFILE = "TAGGED.txt"
counterIndex = 0
indexForTag = 0
# with open(FINALFILE,"w") as file:
  
#     for index in tagMarkedArr:
#         file.write(anotherArrayTag[index] + "\n")


tagFileArr = []
with open(FINALFILE,"r") as file:

    for line in file:
        tagFileArr.append(line.strip())




    # for i in range(len(arrCheck)):
    #     tempTagX = tagMarkedArr[indexForTag]
    #     print(f"this is i: {i} | this is the arr tag: {tempTagX} \n")
    #     if i == tempTagX:
    #         file.write(arrCheck[tempTagX] + "\n")
    #         indexForTag += 1
    #         continue
    #     else:
    #         continue

print("end of program")

        
      





    



    
time.sleep(499)
        
                

with open(uneditedList, "r") as file:
    for line in file:
        iteratorCount+= 1
        tempStr = line
        tempArr.append(line)

        # checking how many special characters there are
        # isalnum()
        for i in range(len(tempStr)):

            if i == "-":
                count += 1

            if count == 0:
                for i in range(len(tempStr)):
                    if i == "-":
                       checkArr.append(newStr)
                       break
                    newStr += tempStr[i]
            elif count == 1:
                for i in range(len(tempStr)):
                    if newCount == 2:
                        checkArr.append(newStr)
                        break
                    if i.isalnum():
                        newCount += 1
                    newStr += tempStr[i]
            else:
                break




print(checkArr)

finalCheck = []
with open(checkFile,"r") as file:
    for line in file:
        finalCheck.append(line)

                   
    

time.sleep(100)  


        
     
            



        # if "-" in line:
        #     if "MXX01" not in line or "RXX01":
        #     textIndex = line.find('-')

        #     if line[textIndex+1] is None:
        #         tempStr = line
        #     else:





           

            # print(line)
            # newFile.append(line)


print(mxxNew)

# print(psdNames)
with open(newFile,"w") as file:
    for i in filenewArr:
        file.write(i)    

time.sleep(100)
# print(psdNames)
# with open(psdtxt,"w") as file:
#     for i in psdNames:
#         file.write(i)

print(arrayNames)
print(type(arrayNames))

newList = []

# for single first name
# print("going through the list of list")
# for sublist in arrayNames:
#     for item in sublist:
#         lineName = sublist[0]
#         print(lineName)
#         newList.append(str(lineName))
#         break

# print(newList)

with open(sortedTest,"w") as file:
    for i in arrayNames:
        file.write(i)
