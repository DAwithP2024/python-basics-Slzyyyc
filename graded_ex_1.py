
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])  # Ascending order
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)  # Descending order

def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price}")

def display_categories():
    print("Categories available:")
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")
    
    category_choice = input("Please select a category (number): ")
    
    if not category_choice.isdigit() or int(category_choice) not in range(1, len(products) + 1):
        print("Invalid selection. Please choose a valid category number.")
        return None
    
    return int(category_choice) - 1  

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))  

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return 0  
    
    total_cost = 0
    cart_output = []
    for product, price, quantity in cart:
        item_cost = price * quantity
        total_cost += item_cost
        cart_output.append(f"{product} - ${price} x {quantity} = ${item_cost}")
    
    
    print("\n".join(cart_output))
    print(f"Total cost: ${total_cost}")
    
    return total_cost  

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def validate_name(name):
    if len(name.split()) != 2 or not all(part.isalpha() for part in name.split()):
        return False
    return True

def validate_email(email):
    return "@" in email

def main():
    cart = []
    

    while True:
        name = input("Please enter your full name: ")
        if validate_name(name):
            break
        print("Invalid name. Please enter your first and last name using only alphabets.")
    

    while True:
        email = input("Please enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email address. Please enter a valid email address.")
    
    
    while True:
        category_index = display_categories()
        
        if category_index is None:
            continue  
        
        selected_category = list(products.keys())[category_index]
        selected_products = products[selected_category]
        
    
        while True:
            display_products(selected_products)
            action_choice = input("1. Select product to buy\n2. Sort products by price\n3. Back to categories\n4. Finish shopping\nChoose an action: ")
            
            if action_choice == '1':
                product_choice = input("Enter the product number: ")
                if not product_choice.isdigit() or int(product_choice) not in range(1, len(selected_products) + 1):
                    print("Invalid product choice.")
                    continue
                
                product = selected_products[int(product_choice) - 1]
                quantity = input("Enter the quantity: ")
                
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity.")
                    continue
                
                add_to_cart(cart, product, int(quantity))
            
            elif action_choice == '2':
                sort_order = input("Sort by price: 1. Ascending 2. Descending\nChoose option: ")
                if sort_order == '1':
                    sorted_products = display_sorted_products(selected_products, "asc")
                elif sort_order == '2':
                    sorted_products = display_sorted_products(selected_products, "desc")
                else:
                    print("Invalid sort order.")
                    continue
                display_products(sorted_products)
            
            elif action_choice == '3':
                break  
            
            elif action_choice == '4':
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Please enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

if __name__ == "__main__":
    main()
