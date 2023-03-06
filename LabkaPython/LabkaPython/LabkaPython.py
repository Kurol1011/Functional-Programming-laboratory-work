name = "Olzhas"
surname = "Kurmangaliev"
#dataOfBirth = "09.03.2003"

print("Имя: " + name)
print("Фамилия: " + surname)

backEndProgrammingLanguage = input("Введите ваш язык программирования:")
age = int(input("Введите ваш возраст: "))
level = "junior"




if(age >= 18):
    print("Вы можете работать полный рабочий день")
else:
    print("Вы можете работать не больше 3 часов в день")

if(backEndProgrammingLanguage == "Java"):
    bestFramework = "Spring"
elif(backEndProgrammingLanguage == "Python"):
    bestFramework = "Django"
elif(backEndProgrammingLanguage == "PHP"):
    bestFramework = "Laravel"
elif(backEndProgrammingLanguage == "JavaScript"):
    bestFramework = "NodeJS"
else:
    bestFramework = ""

print(("Лучший фреймворк для вашего языка для бэкенда это " + bestFramework) if len(bestFramework)>0 else "Вашего языка нету в нашей базе")

