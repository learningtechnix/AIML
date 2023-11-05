from getpass import getpass
import uuid
import random
import time


pre_defined_users = {
    'user1': {'password': 'user1', 'role': 'user'},
    'admin1': {'password': 'admin1', 'role': 'admin'},
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
    print("Username\tRole")
    print(50*"-")
    for username, user_info in pre_defined_users.items():
        print(f"{username}\t{user_info['role']}")
    print()
    time.sleep(1)

def create_user():
    session_id = str(random.randint(100000, 999999))
    new_user_info = {
            'username': input("Enter Username: "),
            'password': getpass("Enter Password: "),
            'role': input("Define Role (admin | user): "),
            'sessionId': session_id
            }
    return new_user_info

def delete_user():
    user_to_delete = input("Enter the username to delete: ")

    if user_to_delete in pre_defined_users:
        del pre_defined_users[user_to_delete]
        print(f"User {user_to_delete} deleted succesfully")
    else:
        print(f"User {user_to_delete} not found")

def display_shopping_catalog():
    print()
    print(50*"-")
    print("Product ID\tName\tCategory ID\tPrice")
    print(50*"-")
    print()
    for product_catalogue in products:
            print(f"{product_catalogue['id']}\t{product_catalogue['name']}\t{product_catalogue['Category']}\t{product_catalogue['price']}")
    print(50*"-")

def add_item_to_catalogue():
    selection = input("Looking to add an Item to Existing category (y|n): ")
    if selection == 'y':
        print()
        print("Displaying existing catalogue for reference")
        display_shopping_catalog()
        print()
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

def del_item_from_catalogue():
    selection = int(input("Kindly share the Product ID of item to delete: "))
    for product in products:
        if product['id'] == selection:
            products.remove(product)
            print()
            print(f"Item {product['name']} with Product ID {product['id']} is successfully removed from {product['Category']} category.")
            time.sleep(2)
            print("Below is the updated catalogue")
            time.sleep(1)
            display_shopping_catalog()
def view_cart(cart_user):
    if not shopping_cart:
        print(40*"*")
        print("Cart is Empty. Feel free to add items")
        print(40*"*")
    else:
        print()
        print(50*"*")
        print(50*"*")
        print(f"Shopping cart of {cart_user}")
        print(50*"*")
        print(50*"*")
        print(f"Id\tName\tQuantity\tItem Price\tTotal Cost")
        for username, cart_items in shopping_cart.items():
            print(f"{cart_items['Product Id']}.\t{cart_items['Item Name']}\t{cart_items['Quantity']}\t{cart_items['Price']}\t{cart_items['Cost']}")
        print(50*"*")

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
                    'Price': product_catalogue['price'],
                    'Cost': total_cost
                    }
            print(50*"*")
            print(f"Item {product_catalogue['name']} is  added successfully to cart")
            print(50*"*")
            time.sleep(2)
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
    print()
    if choice in range(1,6):
        for username, cart_items in shopping_cart.items():
            time.sleep(2)
            print(50*"*")
            print(f"You will be shortly redirected to the portal for Unified Payment Interface to make a payment of Rs. {cart_items['Cost']}")
            print(50*"*")
            time.sleep(1)
    else:
        print("Invalid Option, Exiting ...")


def user_login():
    loginname = input("Enter your username: ")
    loginpass = getpass("Enter Password: ")

    if loginname in pre_defined_users:
        if loginpass == pre_defined_users[loginname]['password']:
            if pre_defined_users[loginname]['role'] == 'user':
                session_id = str(random.randint(900000, 999999))
                while True:
                    print()
                    print(100*"-")
                    print("Welcome {0}! You logged in as \"{1}\" role with sessionID {2}. Kindly choose from below:".format(loginname, pre_defined_users[loginname]['role'], session_id))
                    print(100*"-")
                    print()
                    print("1. View Items into your cart")
                    print("2. Adding Items to cart")
                    print("3. Removing Items from cart")
                    print("4. Making a payment")
                    print("10. Back to main menu")
                    print()
                    choice = input("Select option: ")
                    if choice == '10':
                        welcome_msg()
                        break
                    elif choice == '1':
                        view_cart(loginname)
                        time.sleep(1)
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
                session_id = str(random.randint(100000, 199999))
                while True:
                    print()
                    print("Welcome {0}! You logged in as {1} role. Below are options available for you.".format(loginname, pre_defined_users[loginname]['role']))   
                    print("What operations you are looking to perform ?")
                    print()
                    print(10*"*"," User Role specific options ",10*"*")
                    print("1. View Items into your cart")
                    print("2. Adding Items to cart")
                    print("3. Removing Items from cart")
                    print(30*"*")
                    print()
                    print("4. Displaying catalogue")
                    print("5. Displaying current users")
                    print("6. Create new users")
                    print("7. Delete a user")
                    print("8. Add items to catalogue")
                    print("9. Removing item from catalogue")
                    print("10. Back to main menu")
                    print()
                    choice = input("Select option: ")
                    if choice == '10':
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
                    elif choice == '4':
                        display_shopping_catalog()
                        time.sleep(2)
                    elif choice == '9':
                        del_item_from_catalogue()
                    else:
                        print("Being admin you are not AUTHORIZED to perform this operation , Try again ...")
                        time.sleep(1)
        else:
            print("Login Failed ! {0}, please validate your credentials".format(loginname))
    else:
        print("Username {0} non existent in database".format(loginname))

def welcome_msg():
    while True:
        print()
        print("Welcome to the Demo Marketplace")
        print("*"*30)
        print("For ease of operation, we have provided 2 predefined user, \n'user1' is normal user with password 'user1', \n'admin1' is admin user with password 'admin1'")
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
