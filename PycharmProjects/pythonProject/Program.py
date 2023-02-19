animals = ["Affe", "Gans", "Giraffe", "Zebra", "Nashorn"]
animals_sorted = sorted(animals)
print(animals_sorted)
print(animals)

numbers = [15,2,50,-15]
numbers.sort()
print(numbers)

length = len(animals)
print(f"Länge der Liste: {length}")

animals[1] = "Elefant"
print(animals)

animals.append("Katze")
print(animals)

animals.insert(1, "Hund")
print(animals)

removed_animal = animals.pop(1)
print(animals)
print(removed_animal)

animals.remove("Giraffe")
print(animals)

del animals[1]
print (animals)
