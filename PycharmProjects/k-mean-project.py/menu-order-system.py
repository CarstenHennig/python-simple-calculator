from collections import OrderedDict

menu = OrderedDict()
menu['Sandwich'] = 10
menu['Burger'] = 20
menu['Fries'] = 5
menu['Pizza'] = 25
menu['Salad'] = 15
menu['Coffee'] = 3
menu['Dessert'] = 7

order: str = ''
number_of_order: int = 0
total_of_order: int = 0


def menu_calculate(order, number_of_order, total_of_order=None):
    if order in menu:
        print(f'You ordered: {number_of_order} {order} for {menu[order] * int(number_of_order)}€ in total.')
        total_of_order += (menu[order] * number_of_order)
    else:
        print(f'Sorry, {order} is not available today.')


def menu_order(order, number_of_order):
    order = input("What would you like to order? ")
    number_of_order = input("How many do you want to order? ")

    if order != '' or number_of_order != '':
        menu_calculate(order, number_of_order)
        menu_order(order, number_of_order)
    else:
        print(f'You\'re set. Your complete order is {total_of_order}. Thank you!')
        return


menu_order('Sandwich', 1)
