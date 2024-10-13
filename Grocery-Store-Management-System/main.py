class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class Sale:
    def __init__(self, sale_id, customer_id, product_id, quantity, total_price):
        self.sale_id = sale_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price

class GroceryStore:
    def __init__(self):
        self.products = {}
        self.customers = {}
        self.sales = {}
        self.next_product_id = 1
        self.next_customer_id = 1
        self.next_sale_id = 1

    def add_product(self, name, price, quantity):
        product = Product(self.next_product_id, name, price, quantity)
        self.products[self.next_product_id] = product
        self.next_product_id += 1
        print(f"Product added: {product.name}, ID: {product.product_id}")

    def update_product(self, product_id, name=None, price=None, quantity=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name:
                product.name = name
            if price:
                product.price = price
            if quantity:
                product.quantity = quantity
            print(f"Product updated: {product.name}, ID: {product.product_id}")
        else:
            print(f"Error: Product ID {product_id} not found.")

    def view_products(self):
        if self.products:
            print("\nProduct List:")
            for product in self.products.values():
                print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price:.2f}, Quantity: {product.quantity}")
        else:
            print("No products available.")

    def add_customer(self, name, email):
        customer = Customer(self.next_customer_id, name, email)
        self.customers[self.next_customer_id] = customer
        self.next_customer_id += 1
        print(f"Customer added: {customer.name}, ID: {customer.customer_id}")

    def view_customers(self):
        if self.customers:
            print("\nCustomer List:")
            for customer in self.customers.values():
                print(f"ID: {customer.customer_id}, Name: {customer.name}, Email: {customer.email}")
        else:
            print("No customers available.")

    def record_sale(self, customer_id, product_id, quantity):
        if customer_id not in self.customers:
            print(f"Error: Customer ID {customer_id} not found.")
            return

        if product_id not in self.products:
            print(f"Error: Product ID {product_id} not found.")
            return

        product = self.products[product_id]
        if product.quantity < quantity:
            print("Error: Insufficient product quantity.")
            return

        total_price = product.price * quantity
        sale = Sale(self.next_sale_id, customer_id, product_id, quantity, total_price)
        self.sales[self.next_sale_id] = sale
        self.next_sale_id += 1
        product.quantity -= quantity
        print(f"Sale recorded: Sale ID {sale.sale_id}, Total Price: ${total_price:.2f}")

    def view_sales(self):
        if self.sales:
            print("\nSales List:")
            for sale in self.sales.values():
                print(f"Sale ID: {sale.sale_id}, Customer ID: {sale.customer_id}, Product ID: {sale.product_id}, Quantity: {sale.quantity}, Total Price: ${sale.total_price:.2f}")
        else:
            print("No sales recorded.")

    def save_results(self):
        with open("result.txt", "w") as f:
            if self.products:
                f.write("Products:\n")
                f.write("ID\tName\tPrice\tQuantity\n")
                for product in self.products.values():
                    f.write(f"{product.product_id}\t{product.name}\t${product.price:.2f}\t{product.quantity}\n")
                f.write("\n")
            if self.customers:
                f.write("Customers:\n")
                f.write("ID\tName\tEmail\n")
                for customer in self.customers.values():
                    f.write(f"{customer.customer_id}\t{customer.name}\t{customer.email}\n")
                f.write("\n")
            if self.sales:
                f.write("Sales:\n")
                f.write("Sale ID\tCustomer ID\tProduct ID\tQuantity\tTotal Price\n")
                for sale in self.sales.values():
                    f.write(f"{sale.sale_id}\t{sale.customer_id}\t{sale.product_id}\t{sale.quantity}\t${sale.total_price:.2f}\n")

def main():
    store = GroceryStore()

    while True:
        print("\nGrocery Store Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. View Products")
        print("4. Add Customer")
        print("5. View Customers")
        print("6. Record Sale")
        print("7. View Sales")
        print("8. Save Results")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                store.add_product(name, price, quantity)
            except ValueError:
                print("Error: Invalid price or quantity. Please enter valid numbers.")
        elif choice == 2:
            try:
                product_id = int(input("Enter product ID: "))
                name = input("Enter new product name (leave blank to keep current): ")
                price = input("Enter new product price (leave blank to keep current): ")
                quantity = input("Enter new product quantity (leave blank to keep current): ")
                store.update_product(
                    product_id,
                    name if name else None,
                    float(price) if price else None,
                    int(quantity) if quantity else None
                )
            except ValueError:
                print("Error: Invalid input. Please enter valid values.")
        elif choice == 3:
            store.view_products()
        elif choice == 4:
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            store.add_customer(name, email)
        elif choice == 5:
            store.view_customers()
        elif choice == 6:
            try:
                customer_id = int(input("Enter customer ID: "))
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))
                store.record_sale(customer_id, product_id, quantity)
            except ValueError:
                print("Error: Invalid input. Please enter valid IDs and quantity.")
        elif choice == 7:
            store.view_sales()
        elif choice == 8:
            store.save_results()
            print("Results saved to result.txt")
        elif choice == 9:
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()