import random


#Exercise 1
# data = input()
# print("The original string is : " + str(data))

# sortedString = sorted(set(data))

# print("String after sorting : " + str(sortedString))


#Exercise 2


# library_books = [
#     {'title': 'The Great Gatsby', 'author': 'Fitzgerald', 'year': 1925,'language':'english'},
#     {'title': 'War and peace', 'author': 'Lev Tolstoy', 'year': 1886,'language':'english'},
#     {'title': '1984', 'author': 'George Orwell', 'year': 1949,'language':'english'},
#     {'title': 'The Catcher in the Rye', 'author': 'Salinger', 'year': 1951,'language':'english'},
#     {'title': 'One Hundred Years of Solitude', 'author': 'Marquez', 'year': 1967,'language':'english'}
# ]


# any_published_before_1960 = any(book['year'] < 1960 for book in library_books)

# if any_published_before_1960:
#     print("В библиотеке есть книги, опубликованные до 1960 года")


# all_english_books = all(book.get('language') == 'english' for book in library_books)

# if all_english_books:
#     print("Все книги в библиотеке написаны на английском языке")
# else:
#     print("Есть книги в библиотеке, написанные не на английском языке")

#3

# def rotate_matrix(matrix):
#     transposed = list(zip(*matrix))
#     reversed_rows = [list(reversed(row)) for row in transposed]
#     return reversed_rows

# arr = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]

# res = rotate_matrix(arr)

# #print(res)
# for i in range(len(res)):
#     for j in range(len(res[i])):  
#         print(res[i][j], end=' ')
#     print()

#4

# def getMaxSumBag(weights, values, max_weight):
#     n = len(weights)
#     dp = [0] * (max_weight + 1)
#     for i in range(n):
#         for w in range(max_weight, weights[i] - 1, -1):
#             dp[w] = max(dp[w], dp[w - weights[i]] + values[i]) #Это означает, что мы пытаемся определить, какое будет максимальное значение, если мы добавим текущий предмет в рюкзак вместе с теми предметами, которые уже там есть.
#     return dp[max_weight]

# weights = [1, 2, 3]
# values = [6, 10, 12]
# max_weight = 5
# print(getMaxSumBag(weights, values, max_weight))  


#5
def calcMatrix(matrix1, matrix2, operation):

    result = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    for i, row in enumerate(matrix1):
        for j, element in enumerate(row):
            if operation == "+":
                result[i][j] = element + matrix2[i][j]
            elif operation == "-":
                result[i][j] = element - matrix2[i][j]
            elif operation == "*":
                pairs = zip(matrix1[i], [row[j] for row in matrix2])
                result[i][j] = sum([pair[0] * pair[1] for pair in pairs])

    return result

rows = 3
cols = 4
def getRandMatrix(row,col):
    return [[random.randint(1, 10) for j in range(col)] for i in range(row)]

def showMatrix(mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):  
            print(mtrx[i][j], end=' ')
        print()

mtrx1 = getRandMatrix(rows,cols)
mtrx2 = getRandMatrix(rows,cols)

print("mtrx1: ")
showMatrix(mtrx1)
print("mtrx2: ")
showMatrix(mtrx2)

print()


res = calcMatrix(mtrx1,mtrx2,'+')

for i in range(len(res)):
    for j in range(len(res[i])):  
        print(res[i][j], end=' ')
    print()