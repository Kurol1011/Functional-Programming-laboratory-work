# import random

# #1/1

# studentResume = list()
# isStop = "no"
# while(isStop != "stop"):
#     studentData = input("Enter student data (name, surname, age, email, job, experience year): ")
#     studentResume.append(studentData)
#     isStop = input("if u want stop please write stop if u dont just press enter: ")

# isStop = "no"
# while(isStop != "stop"):
#     print("If you want Find employee by name enter 1 ")
#     print("If you want insert new student on kind position enter 2 ")
#     print("If you want count employee by job and job enter 3 ")
#     print("If you want remove employee by name enter 4 ")
#     print("If you want clear all data enter 5 ")
#     print("If you want stop program enter 0")
#     print("Enter command: ")
#     paramCount = int(input())
#     if(paramCount == 1):
#         studentName = input("Enter student name: ")
#         for i in studentResume:
#             if(i.find(studentName) > -1):
#                 print(i); 
#     elif(paramCount == 2):
#         newStudentData = input("Enter student data (name, surname, age, email, job, experience year): ")
#         position = int(input("Enter position:"))
#         studentResume.insert(position, newStudentData)
#     elif(paramCount == 3):
#         studentJob = input("Enter student job: ")
#         count = 0
#         for i in studentResume:
#             if(i.count(" "+studentJob+" ")>0):
#                 count+=1
#         print(count)
#     elif(paramCount == 4):
#         studentName = input("Enter student name: ")
#         for i in studentResume:
#             if(i.find(studentName) > -1):
#                 studentResume.remove(i)
#     elif(paramCount == 5):
#         studentResume.clear()
#     elif(paramCount == 0):
#         break


# for i in studentResume:
#     print(i)



#1
#//////////////////////////////////////


# class Student:
#      def __init__(self, name, surname, group,age):
#             self.name = name
#             self.surname = surname
#             self.group = group
#             self.age = age

# students = [
#     ("Kail","Bronson","MK-4",18),
#     ("Josh","Makalister","MK-5",19),
#     ("Mike","Targarian","MK-5",21),
#     ("Tom","Stark","MK-5",19),
#     ("Ralf","Lanister","MK-6",20)
# ]


# students.sort(key=lambda student: student[3])
# students.sort(key=lambda student: student[2])
# students.sort(key=lambda student: student[1])
# students.sort(key=lambda student: student[0])

# for i in students:
#     print(i)


#2
#////////////////////////////////////

#1

#////////////////////////////////
#3
#////////////////////////////////
# print("print number:")
# print("if u want stop input enter 0:")
# nums = list()
# num = 1
# while(num !=0):
#     num = int(input())
#     if(num == 0):
#         break
#     nums.append(num)

# print(sorted(nums))


#4
#//////////////////////////////////

# def cmpr1(x,y):
#     return y - x

# print("print number:")
# print("if u want stop input enter 0:")
# nums = list()
# num = 1
# while(num !=0):
#     num = int(input())
#     if(num == 0):
#         break
#     nums.append(num)

# print(sorted(nums,reverse=True))




#5
#/////////////////////////////////////////
# myTicket = {}

# while(len(myTicket)!=24):
#     num = random.randrange(1,49)
#     myTicket.setdefault(num,num)
# print()
# print('my ticket: ' + f'{myTicket.values()}')
# print()

# tirage = {}
# count = 0

# while(len(tirage)!=6):
#     num = random.randrange(1,49)
#     tirage.setdefault(num,num)
# print('tirage: ' + f'{tirage.values()}')
# tirage.clear

# countOfSame = 0
# for i in myTicket.values():
#     for j in tirage.values():
#         if(i == j):
#             countOfSame+=1

# if(countOfSame >=6 ):
#     print(countOfSame)
#     print("Your ticket has win")
# else:
#     print(countOfSame)
#     print("Your ticket has lose")


#6
#//////////////////////////////////////////

# print("print number:")
# print("if u want stop input enter 0:")
# nums = list()
# num = 1
# while(num !=0):
#     num = int(input())
#     if(num == 0):
#         break
#     nums.append(num)

# #print(sorted(nums))

# def isSorted(arr):
#     tempArr = arr
#     if(len(arr)<2):
#         return False
#     i = 0
#     try:
#         while(arr[i] ==arr[i+1]):
#             print("#1")
#             i+=1
#     except Exception:
#         return True
#     if(arr[i] < arr[i+1]):
#         tempArr = sorted(tempArr)
#         print("#2")
#         print(tempArr)
#         print(arr)
#         for i in range(len(arr)):
#             if(tempArr[i] != arr[i]):
#                 return False
#     elif(arr[i] > arr[i+1]):
#         tempArr = sorted(tempArr,reverse=True)
#         print("#3")
#         print(tempArr)
#         print(arr)
#         for i in range(len(arr)):
#             if(tempArr[i] != arr[i]):
#                 return False
#     print("#4")
#     return True

# print(isSorted(nums))