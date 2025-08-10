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
str4 = "UURRF"
str5 = "_fdsajfj"
str6 = "_fdsajfj"
arrC = []

arrC.append(str1)
arrC.append(str2)
arrC.append(str3)
arrC.append(str4)
arrC.append(str5)

tempstring = ""
count = 0
arrCheck = []
for word in arrC:

    tempstring = ""
    for i in range(len(word)):

        char = word[i]

        if "_" in word:
            break

        if char == "-":
            if word[i + 1] is None:
                tempstring = word 
                print(word)
        tempstring += char
 

    print(f"this is the temp string {tempstring}")
    print("\n")
    arrCheck.append(tempstring)
    if count == 0:
        print("where at the first count")
        pass
        
    else:

        print("Checking first word vs seocnd in the arr")
        print(len(arrCheck))
        print(count)
        print(arrCheck)
        print(arrCheck[count - 1])
        print(arrCheck[count])
    
        if arrCheck[count -1 ] == arrCheck[count]:
            print("True")
        else:
            print("False")
    count += 1



print(arrCheck)
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









