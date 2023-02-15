'''
    Python application for a simple calculator,
    asking user whether to start,
    then checking input isnumeric()
    then checking second input = 0 AND operator 0 /
    and asking user to restart or to leave
'''
import math

class Calculator:
    def __init__(self):
        pass

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
        result = math.pow(number_one, 1/number_two)
        return result

calc = Calculator()

def calculation():
    number_one = int(input('Input first number: '))
    number_two = int(input('Input second number: '))
    operator = input('Choose operator: 1 - Add | 2 - Substract | 3 - Multiply | 4 - Divide | 5 - Root 1st num by 2nc num ')
    if operator == '1':
        print(f'{number_one} + {number_two} is {calc.add(number_one, number_two)}')
    elif operator == '2':
        print(f'{number_one} - {number_two} is {calc.substract(number_one, number_two)}')
    elif operator == '3':
        print(f'{number_one} * {number_two} is {calc.multiply(number_one, number_two)}')
    elif operator == '4':
        print(f'{number_one} / {number_two} is {calc.divide(number_one, number_two)}')
    elif operator == '5':
        print(f'Root {number_two} of {number_one} is {calc.root(number_one, number_two)}')

calculation()




"""
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
