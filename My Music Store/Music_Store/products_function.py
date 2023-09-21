products = {
    1: {
        'name': 'Helix',
        'manufacturer': 'Line6',
        'category': 'Guitar Processor',
        'price': 7799,
        'stock': 50
    },
    2: {
        'name': 'Helix LT',
        'manufacturer': 'Line6',
        'category': 'Guitar Processor',
        'price': 5444,
        'stock': 80
    }
}


def add_product():
    product_id = int(input('Please provide a product_id: '))
    print(product_id in products.keys())
    name = input('Please provide a name: ')
    manufacturer = input('Please provide a manufacturer: ')
    category = input('Please provide a category: ')
    price = float(input('Please provide a price: '))
    stock = int(input('Please provide a stock: '))
    product_info = {
        'name': name,
        'manufacturer': manufacturer,
        'category': category,
        'price': price,
        'stock': stock
    }
    products[product_id] = product_info


import main_menu


def remove_product():
    id_remove = int(input("Please insert the ID of the item that you want to remove: "))
    print()
    if id_remove in products.keys():
        print(f'The product that you are trying to remove is: {products[id_remove]["name"]}')
        print()
        response = input("""Do you wish to delete this item?
            1. Yes
            2. No (Delete another product)
            3. Go Back
            """)

        match response:
            case '1':
                del products[id_remove]
            case '2':
                print("Starting the process again...")
                remove_product()
            case '3':
                main_menu.display_second_menu = False
            case _:
                print("No such option!")
    else:
        print("The product you want to remove does not exist in the shop! Please take a better look in our deposit!")
        main_menu.display_second_menu = False


def modify_product():
    id_modify = int(input("Please insert the ID of the item that you want to modify: "))
    print()
    if id_modify in products.keys():
        print(f'The product that you are trying to modify is: {products[id_modify]["name"]}')
        print()
        response = input("""Do you wish to modify this item?
                1. Yes
                2. No (Modify another product)
                3. Go Back
                """)

        match response:
            case '1':
                second_response = input("""What would you like to change at this product?
                        1. Name
                        2. Manufacturer
                        3. Category
                        4. Price
                        5. Stock""")
                match second_response:
                    case '1':
                        new_name = input(f'The current name of the product is: {products[id_modify]["name"]}. What is '
                                         f'the new name of the product?')
                        products[id_modify]["name"] = new_name
                        print(f'The new and modified product is: {products[id_modify]}')
                        main_menu.display_second_menu = False
                    case '2':
                        new_manu = input(
                            f'The current manufacturer of the product is: {products[id_modify]["manufacturer"]}. What is '
                            f'the new manufacturer of the product?')
                        products[id_modify]["manufacturer"] = new_manu
                        print(f'The new and modified product is: {products[id_modify]}')
                        main_menu.display_second_menu = False
                    case '3':
                        new_category = input(
                            f'The current category of the product is: {products[id_modify]["category"]}. What is '
                            f'the new category of the product?')
                        products[id_modify]["category"] = new_category
                        print(f'The new and modified product is: {products[id_modify]}')
                        main_menu.display_second_menu = False
                    case '4':
                        new_price = input(
                            f'The current price of the product is: {products[id_modify]["price"]}. What is '
                            f'the new price of the product?')
                        products[id_modify]["price"] = new_price
                        print(f'The new and modified product is: {products[id_modify]}')
                        main_menu.display_second_menu = False
                    case '5':
                        new_stock = input(
                            f'The current stock of the product is: {products[id_modify]["stock"]}. What is '
                            f'the new stock of the product?')
                        products[id_modify]["stock"] = new_stock
                        print(f'The new and modified product is: {products[id_modify]}')
                        main_menu.display_second_menu = False
                    case _:
                        print("No such option!")
            case '2':
                print("Starting the process again...")
                modify_product()
            case '3':
                main_menu.display_second_menu = False
            case _:
                print("No such option!")
    else:
        print("The product you want to modify does not exist in the shop! Please take a better look in our deposit!")
        main_menu.display_second_menu = False
