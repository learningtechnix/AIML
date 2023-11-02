from getpass import getpass
import uuid
import random


pre_defined_users = {
    'user1': {'password': 'password1', 'role': 'user', 'sessionId': '900001'},
    'admin1': {'password': 'password2', 'role': 'admin', 'sessionId': '100001'},
            }

products = [
        {"Category": "Boots", "id": 1, "name": "Boot1", "price": 50},
        {"Category": "Boots", "id": 2, "name": "Boot2", "price": 60},
        {"Category": "Coats", "id": 3, "name": "Coat1", "price": 100},
        {"Category": "Coats", "id": 4, "name": "Coat2", "price": 120},
        {"Category": "Jackets", "id": 5, "name": "Jacket1", "price": 80},
        {"Category": "Jackets", "id": 6, "name": "Jacket2", "price": 90},
        {"Category": "Caps", "id": 7, "name": "Cap1", "price": 20},
        {"Category": "Caps", "id": 8, "name": "Cap2", "price": 25}
        ]

shopping_cart = {}

def display_users():
    print()
    print(50*"-")
    print("Username\tRole\tSessionID")
    print(50*"-")
    for username, user_info in pre_defined_users.items():
        print(f"{username}\t{user_info['role']}\t{user_info['sessionId']}")
    print()

def create_user():
    session_id = str(random.randint(100000, 999999))
    new_user_info = {
            'username': input("Enter Username: "),
            'password': getpass("Enter Password: "),
            'role': input("Define Role (admin | user): "),
            'sessionId': session_id
            }
    return new_user_info
    #pre_defined_users[new_user_info['username']]

def delete_user():
    user_to_delete = input("Enter the username to delete: ")

    if user_to_delete in pre_defined_users:
        del pre_defined_users[user_to_delete]
        print(f"User {user_to_delete} deleted succesfully")
    else:
        print(f"User {user_to_delete} not found")

def display_shopping_catalog():
    print()
    print("Product ID\tName\tCategory ID\tPrice")
    print(50*"-")
    print()
    for product_catalogue in products:
            print(f"{product_catalogue['id']}\t{product_catalogue['name']}\t{product_catalogue['Category']}\t{product_catalogue['price']}")

def add_item_to_catalogue():
    selection = input("Looking to add an Item to Existing category (y|n): ")
    if selection == 'y':
        update_product_catalogue = {
                'Category': input("Provide category Name: "),
                'name': input("Item name: "),
                'id': int(input("Product ID: ")),
                'price': int(input("Item Price: "))
                }
        return update_product_catalogue
    else:
        new_cat = input("Enter new category you want to add: ")
        update_product_catalogue = {
                'Category': new_cat,
                'name': input("Item name: "),
                'id': int(input("Product ID: ")),
                'price': int(input("Item Price: "))
                }
        return update_product_catalogue

def view_cart(cart_user):
    if not shopping_cart:
        print("Cart is Empty")
    else:
        print()
        print(f"Shopping cart of {cart_user}")
        for username, cart_items in shopping_cart.items():
            print(f"{cart_items['Product Id']}\t{cart_items['Item Name']}\t{cart_items['Quantity']}\t{cart_items['Cost']}")

def add_to_cart():
    print()
    print("Displaying catalogue to select from")
    print()
    display_shopping_catalog()
    print()
    productID = int(input("Enter Product ID of Product to purchase: "))
    quantity = int(input("Enter Quantity you want to purchase: "))
    for product_catalogue in products:
        if productID == int(product_catalogue['id']):
            total_cost = product_catalogue['price'] * quantity
            temporary_shopping_cart = {
                    'username': 'user1',
                    'Product Id': product_catalogue['id'],
                    'Item Name': product_catalogue['name'],
                    'Quantity': quantity,
                    'Cost': total_cost
                    }
            print("Items added successfully to cart")
        else:
            pass
    return temporary_shopping_cart

def delete_from_cart():
    print()
    print()
    user_to_delete = input("Please confirm your username once again for removal: ")
    view_cart(user_to_delete)
    productID = int(input("Enter Product ID of Product to delete: "))
    if user_to_delete in shopping_cart:
        print(f"Item {shopping_cart[user_to_delete]['Item Name']} is deleted successfully")
        del shopping_cart[user_to_delete]['Item Name']
    else:
        print(f"Item with {productID} not found")

def make_payment():
    print()
    print("Select payment option: ")
    print("\t1. Netbanking")
    print("\t2. Debit Card")
    print("\t3. PayPal")
    print("\t4. UPI")
    print("\t5. Pay on Delivery")
    choice = int(input("Enter Choice: "))
    if choice in range(1,6):
        for username, cart_items in shopping_cart.items():
            print(f"You will be shortly redirected to the portal for Unified Payment Interface to make a payment of Rs. {cart_items['Cost']}")
    else:
        print("Invalid Option, Exiting ...")


def user_login():
    loginname = input("Enter your username: ")
    loginpass = getpass("Enter Password: ")

    if loginname in pre_defined_users:
        if loginpass == pre_defined_users[loginname]['password']:
            if pre_defined_users[loginname]['role'] == 'user':
                while True:
                    print()
                    print("Welcome {0}! You logged in as {1} role. Below are options available for you.".format(loginname, pre_defined_users[loginname]['role']))   
                    print("What operations you are looking to perform ?")
                    print()
                    print("1. View Items into your cart")
                    print("2. Adding Items to cart")
                    print("3. Removing Items from cart")
                    print("4. Making a payment")
                    print("9. Back to main menu")
                    print()
                    choice = input("Select option: ")
                    if choice == '9':
                        welcome_msg()
                        break
                    elif choice == '1':
                        view_cart(loginname)
                    elif choice == '2':
                        shopping_cart_temp = add_to_cart()
                        shopping_cart[shopping_cart_temp['username']] = shopping_cart_temp
                    elif choice == '3':
                        delete_from_cart()
                    elif choice == '4':
                        make_payment()
                    else:
                        print("Undefined option, Exiting ...")
                        break
            else:
                while True:
                    print()
                    print("Welcome {0}! You logged in as {1} role. Below are options available for you.".format(loginname, pre_defined_users[loginname]['role']))   
                    print("What operations you are looking to perform ?")
                    print()
                    print("1. View Items into your cart")
                    print("2. Adding Items to cart")
                    print("3. Removing Items from cart")
                    print("4. Making a payment")
                    print("5. Displaying current users")
                    print("6. Create new users")
                    print("7. Delete a user")
                    print("8. Add items to catalogue")
                    print("9. Back to main menu")
                    print()
                    choice = input("Select option: ")
                    if choice == '9':
                        welcome_msg()
                        break
                    elif choice == '5':
                        display_users()
                    elif choice == '6':
                        new_user = create_user()
                        pre_defined_users[new_user['username']] = new_user
                    elif choice == '7':
                        delete_user()
                    elif choice == '8':
                        updated_catalogue = add_item_to_catalogue()
                        products.append(updated_catalogue)
                        print("Displaying updating catalogue")
                        display_shopping_catalog()
                    else:
                        print("Being admin you are not AUTHORIZED to perform this operation , Try again ...")
                        break
        else:
            print("Login Failed ! {0}, please validate your credentials".format(loginname))
    else:
        print("Username {0} non existent in database".format(loginname))

def welcome_msg():
    while True:
        print()
        print("Welcome to the Demo Marketplace")
        print("*"*30)
        print("For ease of operation, we have provided 2 predefined user, \n'user1' is normal user with password 'password1', \n'admin1' is admin user with password 'password2'")
        print("*"*50)
        print()
        print("1. Display shopping catalogue")
        print("2. Login to your account")
        print("7. Exit ....")

        print()
        choice = input("Enter choice: ")

        if choice == '7':
            print("Exiting", "."*10)
            break
        elif choice == '1':
            display_shopping_catalog()
        elif choice == '2':
            user_login()
        else:
            print("Undefined option")
            break

welcome_msg()
