import random

#tuple
# a = ('apple','banana', 'greipfruit','potato',)
# b = (4,6,1,0,8,9,9,)
# print('apple' in a) #1
# #del b #2
# print(b)
# print(a[0:2]) #3 
# print(b.count(9)) #4
# print(a.index("greipfruit"))

#set
# a = {1,2,3,}
# b  = {6,7,8,9}
# a.add(4)
# a.add(5)
# b.add(4)
# b.add(5)
# c = set()
# print(c.union(a,b))

# print(a.difference(b))
# print(a.isdisjoint(b))
# c.update(a)
# print(c.intersection(b))
# print(c.symmetric_difference(b))


#1

# postv = list()
# negtv = list()

# for i in range(10):
#     num = random.randint(0,5)
#     num2 = random.randint(-5,0)
#     postv.append(num)
#     negtv.append(num2)
# a = tuple(postv)
# b = tuple(negtv)
# print(a)
# print(b)
# c = tuple(a + b)
# print(c)
# print(c.count(0))


#2

# a0 = tuple()
# a = ('str',a0,)
# b = (5+4,a,)
# c = (2.54, b,)
# d = (10, c,)

# print(d[1][1][1][0])


#3
# rasxodList = tuple()
# rasxod = tuple(input().split(" "))
# for i in rasxod:
#     rasxodList = rasxodList + (int(i),)
# print(rasxodList)
# sum = 0

# for i in rasxodList:
#     sum+=i
# print(sum)


#4

# str = tuple(input("Students name: ").split(" "))
# names = (str)

# print(names)

# for i in names:
#     if(i.find("ва") > -1):
#         print(i)






#5
# dic = {
# 'а': 'a',
# 'б': 'b',
# 'в': 'v',
# 'г': 'g',
# 'д': 'd',
# 'е': 'e',
# 'ё': 'yo',
# 'ж': 'zh',
# 'з': 'z',
# 'и': 'i',
# 'й': 'y',
# 'к': 'k',
# 'л': 'l',
# 'м': 'm',
# 'н': 'n',
# 'о': 'o',
# 'п': 'p',
# 'р': 'r',
# 'с': 's',
# 'т': 't',
# 'у': 'u',
# 'ф': 'f',
# 'х': 'h',
# 'ц': 'ts',
# 'ч': 'ch',
# 'ш': 'sh',
# 'щ': 'shch',
# 'ъ': 'y',
# 'ы': 'y',
# 'ь': "'",
# 'э': 'e',
# 'ю': 'yu',
# 'я': 'ya',
 
# 'А': 'A',
# 'Б': 'B',
# 'В': 'V',
# 'Г': 'G',
# 'Д': 'D',
# 'Е': 'E',
# 'Ё': 'Yo',
# 'Ж': 'Zh',
# 'З': 'Z',
# 'И': 'I',
# 'Й': 'Y',
# 'К': 'K',
# 'Л': 'L',
# 'М': 'M',
# 'Н': 'N',
# 'О': 'O',
# 'П': 'P',
# 'Р': 'R',
# 'С': 'S',
# 'Т': 'T',
# 'У': 'U',
# 'Ф': 'F',
# 'Х': 'H',
# 'Ц': 'Ts',
# 'Ч': 'Ch',
# 'Ш': 'Sh',
# 'Щ': 'Shch',
# 'Ъ': 'Y',
# 'Ы': 'Y',
# 'Ь': "'",
# 'Э': 'E',
# 'Ю': 'Yu',
# 'Я': 'Ya',}
# text = input("Enter name: ")
# result = ''
# for i in text:
#     if i in dic:
#         result += dic[i]
#     else:
#         result += i
# print(result)