# from car import Car
#
# my_car = Car("Mercedes", "red")
# my_car.describe()
#
# my_car = Car("BMW", "black")
# my_car.describe()
#
#
# my_car.speed = 200
# print(my_car.speed)
#
# my_car.speed = 250
# print(f"The car is running {my_car.speed} km/h.")
#
# my_car.speed = my_car.speed + 30
# print(my_car.speed)
#
# my_car.increase_speed(310)
# print(my_car.speed)

# from vehicle import Vehicle, Plane
#
# # my_vehicle = Plane(800, 10, 7)
# # my_vehicle.drive()
# # print(my_vehicle.door_count)
#
# my_plane = Plane(1000, 3, 8)
# my_plane.drive()
# print(f"Length of wings: {my_plane.wing_length}")



from device import Device, Device_one, Device_two

my_device = Device_one("fan", "hair drying", "blue")
my_device.main_function()
print(my_device.color)
print(f"Device {my_device.name} is {my_device.function} and is {my_device.color}")

my_device = Device_two("vaccum cleaner", "cleaning floors", "pump up")
print(my_device.function_two)
print(f"Device {my_device.name} is {my_device.function} and can {my_device.function_two}")