'''
    Python application for a simple calculator,
    asking user whether to start,
    then checking input isnumeric()
    then checking second input = 0 AND operator 0 /
    and asking user to restart or to leave
'''
import math

memory = 0

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
                result = float(number_one) + float(number_two)
                print('Result is: ', float(number_one) + float(number_two))
            elif operator == '2':
                result = float(number_one) - float(number_two)
                print('Result is: ', float(number_one) - float(number_two))
            elif operator == '3':
                result = float(number_one) * float(number_two)
                print('Result is: ', float(number_one) * float(number_two))
            elif operator == '4':
                result = float(number_one) / float(number_two)
                print('Result is: ', float(number_one) / float(number_two))
            elif operator == '5':
                result = math.sqrt(int(number_one))
                print(f'Root of {number_one} is {math.sqrt(int(number_one))} and root {number_two} of is {math.sqrt(int(number_two))}')
            else:
                print('Invalid input')
            # Ask user to restart or to leave
            global memory
            memory += result
            print('Stored in memory: ', memory)
            use_memory = input('Do you want to del memorized num? 1 - Yes | 2 - No ')
            if use_memory == '1':
                memory = 0
                print(f'Memory is empty -> {memory}')
            else:
                print(f'Memory is still: {memory}')
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
