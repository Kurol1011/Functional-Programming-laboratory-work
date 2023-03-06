str = "This text has been written by Josh Lukas which studied on Satbayev University at 1996 year but now after 27 years ago he still study"

# #1
# print("#1")
# print("true")  if(str.find(" written ") > -1 ) else print("false")

# #2
# print("#2")
# print(str.replace("Satbayev", "MUIT"))


# #3
# print("#3")
# print(str.split(' '))

# #4
# print("#4")
# print(str.isalnum())

# #5
# print("#5")
# print(str.upper())

# # #6
# print("#6")
# print(str.lower())

# #7
# print("#7")
# print(str.count("by"))

# #8
# print("#8")
# print(str.swapcase())

# #9
# print("#9")
# print(str.title())

# # #10
# print("#10")
# for i in range(len(str)):
#     print(f"{ord(str[i])}" + " = " + f"{str[i]}" + " " )




# studentsClass = {
#     1:list(),
#     2:list(),
#     3:list()
# }

# studentsSubjects = {
#     "Math" : list(),
#     "Physics" : list(),
#     "History" : list()
# }

# for i in range(2):
#     studentFullName = input("Enter student full name: ")
#     studentClass = int(input("Enter student class: "))
#     studentSubject = input("Enter student subject: ")

#     if(studentClass in studentsClass.keys()):
#         studentsClass.get(studentClass).append(studentFullName) 
#     else:
#         studentsClass[studentClass] = list()
#         studentsClass.get(studentClass).append(studentFullName)
          
#     if(studentSubject in studentsSubjects.keys()):
#         studentsSubjects.get(studentSubject).append(studentSubject)
#     else:
#         studentsSubjects[studentSubject] = list()
#         studentsSubjects.get(studentSubject).append(studentFullName)

# for i in studentsClass.keys():
#     print(f'{i}) {studentsClass.get(i)}')







# str = input("Enter str: ")
# bigAlp = 0
# smallAlp = 0
# for i in range(len(str)):
#     if(str[i].isupper()):
#         bigAlp+=1
#     elif(str[i].islower()):
#         smallAlp+=1

# if(bigAlp > smallAlp):
#     print(str.upper())
# elif(bigAlp < smallAlp):
#     print(str.lower())
# elif(bigAlp == smallAlp):
#     print(str)






# break_out_flag = True
# while(break_out_flag):
#     a = input("Enter number a: ")
#     if(a.isdigit()):
#         while(break_out_flag):
#             b = input("Enter number b: ")
#             if(b.isdigit()):
#                 print(int(a) + int(b))
#                 break_out_flag = False
    
