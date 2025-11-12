# A shopping application that allows users to register and place orders from a list of available items.
print("Welcome to the Shopping App!")

username = input("Enter your username: ")
while len(username) < 5:
    print("Username must be at least 5 characters long.")
    username = input("Enter your username: ")



password = input("Enter your password: ")
while len(password) < 8:
    print("Password must be at least 8 characters long.")
    password = input("Enter your password: ")

email = input("Enter your email address: ")
while "@" not in email or "." not in email:
    print("Please enter a valid email address.")
    email = input("Enter your email address: ")

print(f"Welcome, {username}! Your registration is complete.")

items_available = ["Cold Drinks", "Snacks", "Sandwiches", "Salads", "Desserts", "Coffee", "Tea", "Juices"]

for item in items_available:
    print(f"Items available - {item}")

order_list = []
not_available = []

item_requested = input("Enter the items you want to order (q to place order): ")

while item_requested != 'q':
    if item_requested in items_available:
        print(f"Adding {item_requested} to your order.")
        order_list.append(item_requested)
    else:
        print("Sorry, we don't have that item. Please choose from the available items.")
        not_available.append(item_requested)
    
    item_requested = input("Enter the items you want to order (q to place order): ")

print("Placing your order. Thank you!")
if order_list:
    print(f"Your order: {', '.join(order_list)}")
    print(f"Reporting unavailable items: {', '.join(not_available)}")
else:
    print("No items ordered.")





