#1.0
# import random
# colors = {
#     1: "red",
#     2: "black",
#     3: "green",
#     10: "yellow"
# }

# print(colors.items())
# print("-------------")
# print(colors.keys())
# print("-------------")
# for i in range(len(colors)):
#     print(colors.get(i,"error"))
# print("-------------")
# for i in range(len(colors)):
#     print(colors.setdefault(i,"white"))
# print("-------------")
# for i in range(len(colors)):
#     if(colors.get(i,0)!=0):
#         print(colors.pop(i))
# print("-------------")
# print(colors)



#1.1

# N = int(input("Enter number N: "))
# countryAndRivers = {
#     "Qazaqstan" : list(),
#     "Kyrgizstan" : list(),
#     "Spain" : list()
# }

# # qaz : "Syrdariya", "Nura", "Sarysu",  #comment
# #kgz : "Kugart","Sokuluk" #comment
# #spn: "Duero","Ebro","Taho" #comment

# rivers = ["Taho","Syrdariya", "Nura","Duero","Kugart","Sokuluk","Ebro","Sarysu"]

# for i in rivers:
#     country = input(i + " - What country does this river belong to? : " )
#     if(countryAndRivers.get(country,0) != 0):
#         countryAndRivers.get(country,0).append(i)
#     else:
#         print("this doesnt exist on dict")

# for i in range(N):
#     flag = False
#     river = input("Enter river name to check is exist in dict or not: ")
#     for i in countryAndRivers:
#         for j in countryAndRivers.get(i):
#             if(j == river):
#                 print("This river is exist in dict")
#                 flag = True
#                 break
#         if(flag):
#             break
#     if(flag == False):
#         print("This river isn't exist in dict")

# for i in range(N):
#     countryRiver = input("Enter country then river: ")
#     countryAndRivers.setdefault(countryRiver.split(" ")[0], [countryRiver.split(" ")[0]])

# for i in countryAndRivers:
#     print(i + ": ")
#     print(countryAndRivers.get(i))
#     print()



#2
# print("Enter comments with name: ")
# nameAndComment = input()
# dataName = {}
# while(len(nameAndComment) != 0):
#     if(dataName.get(nameAndComment.split(":")[0],0) == 0):
#         dataName.setdefault(nameAndComment.split(":")[0],1)
#     else:
#         sum = dataName.get(nameAndComment.split(":")[0]) + 1
#         dataName.pop(nameAndComment.split(":")[0])
#         dataName.setdefault(nameAndComment.split(":")[0], sum)
#     nameAndComment = input()
# print(dataName)
# print(len(dataName.keys()))
    

#3

# countTelNumber = int(input("Enter count of phone number: "))
# dataPhoneNum = {}
# for i in range(countTelNumber):
#     nameAndPhoneNum = input("Enter name then his phone number: ")
#     dataPhoneNum.setdefault(nameAndPhoneNum.split(" ")[0],nameAndPhoneNum.split(" ")[1])

# str = input("Enter name: ")
# while(str!="stop"):
#     if(dataPhoneNum.get(str,0) !=0):
#         print(dataPhoneNum.get(str))
#     else:
#         print("Name is not found in data numbers")
#     str = input("Enter name or stop for stop programm: ")
# print("Program has stopped!")

#4

graphicVacation = {}

countOfEmployee = int(input("Enter count of employee: "))

for i in range(countOfEmployee):
    dataEmployee = input("Enter employee surname day_vacation month_vacation: ")
    if(graphicVacation.get(dataEmployee.split(" ")[2],0) != 0):
        graphicVacation.get(dataEmployee.split(" ")[2]).append(dataEmployee)
    else:
        graphicVacation.setdefault(dataEmployee.split(" ")[2],[dataEmployee])

keyDict = input("enter month vacation: ")
print(graphicVacation.get(keyDict),"")

        
