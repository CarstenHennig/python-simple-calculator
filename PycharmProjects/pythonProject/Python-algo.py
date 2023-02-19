numbers = list(range(1,10001))
list_a = []
list_b = []

for number in numbers:
    if number % 5 == 0:
        list_a.append(number)
    else:
        list_b.append(number)

print(list_a)
print(list_b)