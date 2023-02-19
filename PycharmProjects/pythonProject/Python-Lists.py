food = []
food.append("Lasagne")
food.append("Pasta")
food.append("Maccaroni")

print(food)

food.pop()
print(food)

food.insert(1, "Lebkuchen")
print(food)

print(food[-1])

food.sort(reverse=True)
print(food)