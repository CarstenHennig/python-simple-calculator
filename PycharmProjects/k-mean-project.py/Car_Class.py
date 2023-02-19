class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'The {self.color} car has {self.mileage} miles.'


blue_car = Car(color='blue', mileage=20_000)
red_car = Car('red', 30000)

blucar = Car('blue', 25000)
recar = Car('red', 35000)
print(blucar)
print(recar)

for car in (blue_car, red_car):
    print(f'The {car.color} car has {car.mileage} miles.')


class Dogs:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Our dog {self.name} is {self.age} years old'


dog1 = Dogs('Hector', 4)
dog2 = Dogs('Conda', 7)

print(dog1)
print(dog2)
