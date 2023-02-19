# person = {
#     "name": "Jannick",
#     "height": 180,
# }
#
# persons = [
#     {
#         "name": "Jannick",
#         "height": 180,
#     },
#     {
#         "name": "Peter",
#         "height": 190,
#     },
#     {
#         "name": "Klara",
#         "height": 169,
#     }
# ]
#
# for person in persons:
#     print(f"Name ist {person['name']} und Körpergröße in cm ist {person['height']}")


# animal = {
#     "name": "Berta",
#     "type": "Giraffe"
# }
#
# animal["partner"] = {
#     "name": "Helmut",
#     "type": "Giraffe",
#     "hasChildren": True
# }

# print(animal["partner"]["hasChildren"])
#
# del animal["type"]
# print(animal)
#
# users = ["Jannick", "Peter", "Karl"]
#
# banned_users = {
#     "Jannick": False,
#     "Karl": False,
#     "Peter": True
# }
#
# print(banned_users.get("Peter", True))
#
# for key, value in banned_users.items():
#     if value == True:
#         print(f"{key} ist banned")
#     else:
#         print(f"{key} ist dabei")
#
#
# students = {
#     "Jannick": 36335,
#     "Peter": 24543,
#     "Klara": 16423
# }
#
# for key, value in students.items():
#     print(f"Key: {key}, Value: {value}")
#
# for value in students.values():
#     print(f"Value ist: {value}")
#
# studis = [
#     {
#         "name": "Jannick",
#         "age": 28,
#         "matricle_number": 35654
#     },
#     {
#         "name": "Peter",
#         "age": 27,
#         "matricle_number": 24536
#     },
#     {
#         "name": "Clara",
#         "age": 30,
#         "matricle_number": 14563
#     }
# ]
#
# print(studis)
#
# for student in studis:
#     for key, value in student.items():
#         print(f"Key ist: {key}, Value: {value}")
#
#

payroll = [
    {
        "name": "Jan",
        "profession": "Maler",
        "payment": 4000
    },
    {
        "name": "Heinz",
        "profession": "Klempner",
        "payment": 3000
    },
    {
        "name": "Elisabeth",
        "profession": "Controllerin",
        "payment": 5000
    },
    {
        "name": "Eva",
        "profession": "Azubi",
        "payment": 1500
    },
    {
        "name": "Heinz-Uwe",
        "profession": "Geschäftsführer",
        "payment": 6000
    }
]

pay_sum = 0

for pay in payroll:
    print(pay["name"], pay["profession"], pay["payment"])
    pay_sum += pay["payment"]

print(f"Payroll total: {pay_sum}€")
