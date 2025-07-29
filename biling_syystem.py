products = [
    {"name": "shose", "price": "$300", "quantity": 30},
    {"name": "headphone", "price": "$10", "quantity": 30},
    {"name": "remote", "price": "$5", "quantity": 30}
]

total_bill = 0   

print("---- List Products ----")
print("1. Show Products")
print("2. Pay Products")
print("3. Show Bill")
print("4. Exit")

while True:
    choice = input("\nChoose from the list: ")

    if choice == '1':
        print("---- Available Products ----")
        for product in products:
            print(f"Name: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")

    elif choice == '2':
        product_name = input("Enter the product name you want to buy: ").lower()
        quantity = int(input("Enter the quantity: "))
        found = False

        for product in products:
            if product['name'].lower() == product_name:
                found = True
                if quantity <= product['quantity']:
                    price_num = int(product['price'].strip('$'))
                    total_price = price_num * quantity
                    product['quantity'] -= quantity
                    total_bill += total_price
                    print(f"Added to your bill: {product['name']} x {quantity} = ${total_price}")
                else:
                    print("Sorry, not enough quantity in stock.")
                break

        if not found:
            print("Product not found.")

    elif choice == '3':
        print(f"Your total bill is: ${total_bill}")

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
