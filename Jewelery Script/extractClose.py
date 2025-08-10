import os
import re 
import time


# MXX01X
# RXX01

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
# i need to append string first then check.

str1 = "MXXX01-IIII"
str2 = "MXXX01-IIII2"
str3 = "UURRF"
str4 = "UURRF444"
str5 = "_fdsajfj"
str6 = "_fdsajfj"
str7 = "aaa"
str8 = "aaa"
str9 = "MXXX01-IIII"
str10 = "MXXX01-IIII"
str11 = "MXXX01-IIII-3-5"
str12 = "MFHSADFJ-"
str13 = "MFHSADFJ234234-"
arrC = []

arrC.append(str1)
arrC.append(str2)
arrC.append(str3)
arrC.append(str4)
arrC.append(str5)
arrC.append(str6)
arrC.append(str7)
arrC.append(str8)
arrC.append(str9)
arrC.append(str10)
arrC.append(str11)
arrC.append(str12)
arrC.append(str13)

tempstring = ""
count = 0
arrCheck = []
indexArr = 0
for word in arrC:
    if "_" in word:
        pass

    else:
        tempstring = ""
        charCount = 0
        for i in range(len(word)):
        
            char = word[i]

            if "_" in word:
                break
            
            try:
                if char == "-":
                    print("this is the char count")
                    print(charCount)
                    charCount += 1

                    if word[i + 1] is None:
                        tempstring = word 
                        print(word)
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
            indexArr += 1
            arrCheck.append(tempstring)
            
        if count == 0:
            print("where at the first count")
            pass
        else:
            pass
             
        count += 1


print("arrayCheck below")
print(arrCheck)
print("\n")

# arrayCheck below
# ['MXXX01-IIII', 'MXXX01-IIII2', 'UURRF', 'UURRF444', 'aaa', 'aaa', 'MXXX01-IIII', 'MXXX01-IIII', 'MXXX01-IIII', 'MFHSADFJ-', 'MFHSADFJ234234-']
lengthOfArray = len(arrCheck) - 1
markerArr = []
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
                print(arrCheck)
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
for index in markerArr:
    num = index
    print(arrCheck[num])

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









