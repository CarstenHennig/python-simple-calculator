class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 100

    def drive(self):
        print(f"{self.color} car is running")

    def describe(self):
        print(f"The car has the color {self.color} and is a {self.brand}.")

    def increase_speed(self, new_value):
        if new_value > 300:
            print("Zu schnell")
            return
        self.speed = new_value
