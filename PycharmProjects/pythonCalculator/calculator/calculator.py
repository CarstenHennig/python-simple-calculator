"""
    Python application for a simple calculator,
    asking user whether to start,
    then checking input isnumeric()
    then checking second input = 0 AND operator 0 /
    and asking user to restart or to leave
"""

'''
THIRD TRY - Feb 19, 2023
'''


class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def nth_root(self, x, n):
        if x < 0 and n % 2 == 0:
            raise ValueError("Cannot take even root of negative number")
        return x ** (1 / n)

    def memory_store(self, x):
        self.memory = x

    def memory_recall(self):
        return self.memory


'''
You can then create an instance of the Calculator class and use its methods to perform calculations:
'''

calc = Calculator()

# Input int for calculation
number_one = int(input('First number: '))
number_two = int(input('Second number: '))

# First instance: Adding
result = calc.add(number_one, number_two)
print(f' {number_one} + {number_two} = {result}')

# Second instance: Subtracting
result = calc.subtract(number_one, number_two)
print(f' {number_one} - {number_two} = {result}')

# Third instance: Multiply
result = calc.multiply(number_one, number_two)
print(f' {number_one} * {number_two} = {result}')

# Fourth instance: Divide
result = calc.divide(number_one, number_two)
print(f' {number_one} / {number_two} = {result}')

# Fifth instance: n-th root
result = calc.nth_root(number_one, number_two)
print(f' N-th root of {number_one} and {number_two} = {result}')

# Sixth instance: memory
calc.memory_store(number_one)
calc.memory_store(number_two)
result = calc.memory_recall()
print(f'Memory: {result}')

''' Unit testing with assert '''
assert (calc.add(1, 2) == 3)
assert (calc.subtract(20, 3) == 17)
assert (calc.multiply(4, 5) == 20)
assert (calc.divide(30, 10) == 3)
assert (calc.nth_root(20, 17) == 1.1926998818042585)

'''
Note that the divide method raises a ValueError if the second argument is zero, to avoid a division by zero error. 
Also, the nth_root method checks for cases where the input is negative and the root is even, which would result in a complex number. 
Finally, the memory_store and memory_recall methods are used to store a value in memory and retrieve it later.
'''

'''
SECOND TRY - Feb 15, 2023
#########################

import math

memory = 0  # initialize memory to 0
result = 0
number_one: float = 0
number_two: float = 0

class Calculator:
    def __init__(self, memory: float = 0.0) -> None:
        self._memory = memory

    def add(self, number_one, number_two):
        result = number_one + number_two
        return result

    def substract(self, number_one, number_two):
        result = number_one - number_two
        return result

    def multiply(self, number_one, number_two):
        result = number_one * number_two
        return result

    def divide(self, number_one, number_two):
        result = number_one / number_two
        return result

    def root(self, number_one, number_two):
        result = math.pow(number_one, 1 / number_two)
        return result

    def add_to_memory(result):
        global memory  # use the global variable 'memory'
        memory += result

    def subtract_from_memory(result):
        global memory  # use the global variable 'memory'
        memory -= result

    def recall_memory():
        return memory


calc = Calculator()


def calculation():
    number_one = int(input('Input first number: '))
    number_two = int(input('Input second number: '))
    operator = input(
        'Choose operator: 1 - Add | 2 - Substract | 3 - Multiply | 4 - Divide | 5 - Root 1st num by 2nc num ')
    if operator == '1':
        result = calc.add(number_one, number_two)
        print(f'{number_one} + {number_two} is {result}')
    elif operator == '2':
        result = calc.substract(number_one, number_two)
        print(f'{number_one} - {number_two} is {calc.substract(number_one, number_two)}')
    elif operator == '3':
        print(f'{number_one} * {number_two} is {calc.multiply(number_one, number_two)}')
    elif operator == '4':
        print(f'{number_one} / {number_two} is {calc.divide(number_one, number_two)}')
    elif operator == '5':
        print(f'Root {number_two} of {number_one} is {calc.root(number_one, number_two)}')

    print(result)
    activate_memory = int(input('1 - Add result to memory | 2 - Substract result from memrory | 3 - Recall memory '))
    if activate_memory == 1:
        Calculator.add_to_memory(result)
        print(memory)
    elif activate_memory == 2:
        Calculator.subtract_from_memory(result)
        print(memory)
    elif activate_memory == 3:
        Calculator.recall_memory(result)
        print(memory)
    else:
        print('Wrong input')

calculation()
'''

"""
FIRST TRY - Feb 13, 2023
########################
def calculation():
    # Ask user for number input
    number_one = input('Input your first number: ')
    # Check if input isnumeric
    if number_one.isnumeric():
        number_two = input('Input your second number: ')
        if number_two.isnumeric():
            # Ask user choosing an operator
            print(f' 1 - add | 2 - substract | 3 - multiply | 4 - divide | 5 - root')
            operator = input('Choose your operator: ')

            # Calculate and print result
            if number_two == '0' and operator == "3":
                print('Dividing by 0 not allowed. Try again!')
                calculation()
            elif operator == '1':
                result = calc.add(int(number_one), int(number_two))
                print(f'{number_one} plus {number_two} = {result}')
            elif operator == '2':
                result = calc.substract(int(number_one), int(number_two))
                print(f'{number_one} minus {number_two} = {result}')
            elif operator == '3':
                result = calc.multiply(int(number_one), int(number_two))
                print(f'{number_one} multiplied with {number_two} = {result}')
            elif operator == '4':
                result = calc.divide(int(number_one), int(number_two))
                print(f'{number_one} divided by {number_two} = {result}')
            elif operator == '5':
                result = calc.root(int(number_one))
                print(
                    f'Root of {number_one} and {number_two} = {calc.root(int(number_one))}, {math.sqrt(int(number_two))}')
            else:
                print('Invalid input')
            # Ask user to restart or to leave
            global memory
            memory.append(result)
            print('Stored in memory: ', result)
            use_memory = input('Do you want to del memorized num? 1 - Yes | 2 - No ')
            if use_memory == '1':
                memory.pop()
                print(f'Last item in memory deleted. Memory is {memory}')
            else:
                print(f'Stored in memory: {memory}')
            starter_again = input('Do you want to start again? 1 - Yes | 2 - No ')
            if starter_again == '1':
                calculation()
            elif starter_again == '2':
                print('C U next time!')
            else:
                print('Invalid input')
                calculation()
        else:
            print(f'{number_two} is invalid! It is empty or contains a string. ONLY NUMBERS are allowed!')
            calculation()
    else:
        print(f'{number_one} is invalid! It is empty or contains a string. ONLY NUMBERS are allowed!')
        calculation()


# Initializing function calculator
print('This is your calculator')
starter = input('Do you want to start? 1 - Yes | 2 - No ')
if starter == '1':
    calculation()
else:
    # Asking user to leave or to restart
    print('Are you a spoilsport?')
    try_again = input('1 - Yes, I fear ... | 2 - Of course, not! ')
    if try_again == '2':
        print('Great! Let\'s start again!')
        calculation()
    elif try_again == '1':
        print('C U next time')
    else:
        print('Invalid input')
        calculation()

"""
