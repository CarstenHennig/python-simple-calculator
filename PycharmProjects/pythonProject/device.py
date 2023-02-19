class Device:

    def __init__(self, name, function):
        self.name = name
        self.function = function

    def main_function(self):
        print(f"No function")

class Device_one(Device):

    def __init__(self, name, function, color):
        super().__init__(name, function)
        self.color = color

class Device_two(Device):

    def __init__(self, name, function, function_two):
        super().__init__(name, function)
        self.function_two = function_two
