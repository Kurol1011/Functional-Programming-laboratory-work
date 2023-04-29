# #1
# import os

# db_file = "library_database.txt"


# def add_book(title, author, genre):
#     with open(db_file, "a") as f:
#         f.write(f"{title},{author},{genre}\n")


# def remove_book(title):
#     with open(db_file, "r") as f:
#         lines = f.readlines()
#     with open(db_file, "w") as f:
#         for line in lines:
#             if not line.startswith(title):
#                 f.write(line)


# def search_book(title):
#     with open(db_file, "r") as f:
#         for line in f:
#             if line.startswith(title):
#                 return line.strip().split(",")
#     return None


# def list_books():
#     with open(db_file, "r") as f:
#         for line in f:
#             title, author, genre = line.strip().split(",")
#             print(f"{title} by {author} ({genre})")


# def edit_genre(title, new_genre):
#     with open(db_file, "r") as f:
#         lines = f.readlines()
#     with open(db_file, "w") as f:
#         for line in lines:
#             if line.startswith(title):
#                 title, author, _ = line.strip().split(",")
#                 f.write(f"{title},{author},{new_genre}\n")
#             else:
#                 f.write(line)


# if not os.path.exists(db_file):
#     with open(db_file, "w") as f:
#         f.write("")


# add_book("The Lord of the Rings", "Tolkien", "Fantasy")
# add_book("Harry Potter", "J.K. Rowling", "Fantasy")
# add_book("1984", "Orwell", "Dystopia")
# add_book("Snowman", "otto", "detective")
# list_books()
# remove_book("1984")
# list_books()
# edit_genre("Snowman", "horror")
# list_books()


#2


# with open('GirlNames.txt',encoding='utf-8') as f:
#     girl_names = f.read().splitlines()

# with open('BoyNames.txt',encoding='utf-8') as f:
#     boy_names = f.read().splitlines()




# name = input('Введите имя мальчика, имя девочки или оба имени: ')


# if name in boy_names:
#     print(f'{name} является одним из самых популярных имен для мальчиков.')
# if name in girl_names:
#     print(f'{name} является одним из самых популярных имен для девочек.')
# if name not in boy_names and name not in girl_names:
#     print(f'{name} не является одним из самых популярных имен для мальчиков или девочек.')

#3

# import string

# def count_words(filename):
    
#     word_count = {}
#     stop_words_1 = ["для", "на", "по", "со", "из", "от", "до", "без", "над", "под", "за", "при", "после", "во","и",'в',"с"]
#     stop_words_2 = ["он", "мы", "его", "вы", "вам", "вас", "ее", "что", "который", "их", "все", "они", "я", "весь", "мне", "меня", "таким"]
#     stop_words_3 = ["не", "же", "то", "бы", "всего", "итого", "даже", "да", "нет"]
    
#     with open(filename, 'r',encoding='utf-8') as f:
#         text = f.read()

#     text = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

    
    
#     text = [txt for txt in text if txt not in stop_words_1 and stop_words_2 and stop_words_3]

    
#     for word in text:
#         if word not in word_count:
#             word_count[word] = 0
#         word_count[word] += 1

    
#     sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
#     for word, count in sorted_words:
#         print(word, count)


# count_words('obrabotka.txt')

#4

# import datetime


# with open("dates.txt") as file:
#     dates = file.read().splitlines()


# today = datetime.date.today()


# date_diffs = {}
# for date in dates:
#     date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
#     diff = abs((today - date_obj).days)
#     date_diffs[date] = diff


# sorted_dates = sorted(date_diffs.items(), key=lambda x: x[1])


# for date, diff in sorted_dates:
#     print(date)

#5
# import csv


# with open('zabolevaemost.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter='\t') 
#     region_cases = {} 
#     for row in reader:
#         region = row['Город']
#         cases = int(row['Кол-во заболевших'])
#         region_cases[region] = cases
    
    
#     sorted_regions = sorted(region_cases, key=region_cases.get, reverse=True)
    
    
#     max_cases = region_cases[sorted_regions[0]]
#     for region in sorted_regions:
#         if region_cases[region] == max_cases:
#             print(region)
#         else:
#             break




