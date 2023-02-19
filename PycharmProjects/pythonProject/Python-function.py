
# def greet(name):
#     print(f"Hello {name}")
#
# greet("Jan")
# greet("Klara")

# books = []
#
# def addBook(book):
#     books.append(book)
#
# addBook("Harry Potter 1")
# addBook("Learn Python")
# print(books)

# def log_student(name, major = "Informatik"):
#     print(f"Der Student heißt {name} und sein Hauptfach ist {major}.")
#
# log_student("Peter", "Mathe")

# def build_student(name, major = "Mathe"):
#     person = {"person_name" : name, "person_major" : major}
#     return person
#
# my_person = build_student("Peter", "Informatik")
# print(my_person)
#
#
# def add(a, b):
#     # result = a + b
#     # return result
#     return a + b
#
# my_result = add(5, 10)
# print(my_result)


cars = []

def build_car(marke, farbe, preis, tueren = 5):
    car = { "marke" : marke, "farbe" : farbe, "preis" : preis, "tueren" : tueren}
    return car

cars.append(build_car("VW", "rot", "40000"))
cars.append(build_car("Audi", "blau", "60000", 3))
cars.append(build_car("Mercedes", "schwarz", "100000"))
print(cars)

