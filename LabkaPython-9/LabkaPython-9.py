from functools import reduce
#1,2,3 exercise

# class Student:
#     def __init__(self, id, name, surname, lessons, grades):
#         self.id = id
#         self.name = name
#         self.surname = surname
#         self.lessons = lessons
#         self.grades = grades

# students = (
#     Student(1, "Michael", "Armanski", ["math", "physics", "history"], {"math": 5, "physics": 4, "history": 3}),
#     Student(2, "Jazira", "Katya", ["math", "history"], {"math": 4, "history": 5}),
#     Student(3, "Arman", "Su", ["physics", "history"], {"physics": 3, "history": 4}),
# )

# def get_top_student(students):
#     top_student = None
#     top_grade_avg = -1
#     for student in students:
#         grade_avg = sum(student.grades.values()) / len(student.grades)
#         if grade_avg > top_grade_avg:
#             top_grade_avg = grade_avg
#             top_student = student
#     return top_student

# top_student = get_top_student(students)


# studentsWithFiveGrades = list(filter(lambda s: 5 in s.grades.values(), students))


# if studentsWithFiveGrades:
#     print(f"Students with grade 5:")
#     for student in studentsWithFiveGrades:
#         print(f"{student.name} {student.surname}: {student.lessons} - {student.grades}")
# else:
#     print("No students with grade 5")
# print('end')
# print()
# print(f"Students group:")
# list(map(lambda s: print(f"{s.name} {s.surname}: {s.lessons} - {s.grades}"), students))
# print('end')
# print()
# print(f"The top student is {top_student.name} {top_student.surname}, with an average grade of {sum(top_student.grades.values()) / len(top_student.grades):.2f}")
# print(f"His lessons:{top_student.lessons}")
# print(f"His grades:{top_student.grades}")

# def getAvgStudents(students):
#     total_grades = reduce(lambda acc, s: acc + sum(s.grades.values()), students, 0)
#     avg_grade = total_grades / sum(len(s.grades) for s in students)
#     print(f"Average grade: {avg_grade:.2f}")

# getAvgStudents(students)


#Exercise 4

# def getDeliveryCost(street_name, product_price):
#     square_streets = ["Аль-Фараби", "Саина", "Ташенова", "Достык"]
#     inSquare = list(filter(lambda s: s.find(street_name.split(' ')[0])>-1 , square_streets))
#     if len(inSquare) > 0:
#         if product_price < 10000:
#             return 500
#         else:
#             return 0
#     else:
#         if product_price < 10000:
#             return 1000
#         else:
#             return 1000

# street = "Аль-Фараби 185a"
# price = 7500

# delivery_cost = getDeliveryCost(street, price)
# print(f"The delivery cost for {street} and a product with a price of {price} is {delivery_cost} tenge.")


#Exercise 5
def combo(f, g):
    def h(x):
        return f(g(x))
    return h

students = [
    {"name": "Michael", "surname": "Armanski", "average_grade": 4.5},
    {"name": "Jazira", "surname": "Katya", "average_grade": 3.8},
    {"name": "Arman", "surname": "Su", "average_grade": 4.2},
]

def select_students(students, threshold):
    return [s for s in students if s["average_grade"] >= threshold]

def sort_students(students):
    return sorted(students, key=lambda s: s["surname"])

new_function = combo(sort_students, lambda students: select_students(students, 4.0))

result = new_function(students)

print(result)


