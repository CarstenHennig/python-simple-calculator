# counter = 0
#
# while counter < 5:
#     counter += 1
#     print(counter)

# cars = [
#      "BMW", "Audi", "BMW", "Mercedes", "BMW", "Toyota"
# ]
#
# print(cars)
#
# while "BMW" in cars:
#     cars.remove("BMW")
#
# print(cars)


# print("Willkommen, stellt Euch vor!")
#
# user_input = ""
# students = []
# while user_input != "quit":
#     user_input = input("Dein Name: ")
#
#
#     if user_input != "quit":
#         print(f"Hallo {user_input}!")
#         students.append(user_input)
#
# print("Wir sind vollzählig. Lasst uns beginnen")
#
# for student in students:
#     print(f"Danke und bis bald, {student}!")


# print("Even or odd?")
#
# number = ""
#
# while True:
#
#     number = input()
#
#     if number == "quit":
#         print("Bye")
#         break
#     else:
#         digit = int(number)
#
#         if digit % 2 == 0:
#             print("Number is even")
#         else:
#             print("Number is odd")

payroll = {}

while True:
    new_employee = input("Name of employee: ")
    new_salary = int(input("What's salary: "))

    payroll[new_employee] = new_salary

    if len(payroll) == 2:
        print("Voll")
        break

print(payroll)
for pay in payroll:
    print(f"Name: {pay}, Salary: {value}")
