MAIN_MENU = """
1. Products
2. Clients
3. Transactions
4. Reports
X. Exit
"""

PRODUCTS_MENU = """
1. Add
2. Remove
3. Update
4. Display all
x. Go Back
"""

import products_function

while True:
    print(MAIN_MENU)

    option = input('Select an option from the menu: ').lower()

    match option:
        case '1':
            display_second_menu = True
            while display_second_menu:
                print(PRODUCTS_MENU)
                option = input('Select an option from the product menu: ').lower()
                print()
                match option:
                    case '1':
                        products_function.add_product()
                    case '2':
                        products_function.remove_product()
                    case '3':
                        products_function.modify_product()
                    case '4':
                        print(products_function.products)
                    case 'x':
                        print('Back')
                        display_second_menu = False
                    case _:
                        print('No such option!')

        case '2':
            print('Client')
        case '3':
            print('Transactions')
        case '4':
            print('Reports')
        case 'x':
            print('Exiting')
            break
        case _:
            print('No such option!')
