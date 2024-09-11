#Layyana Junaid 23k-0056
#Lab 4 task 5
#creating a restaurant class situation 

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_menu_items(self, menu_item, price):
        self.menu_items[menu_item] = price
        print(f"Added '{menu_item}' to the menu with price ${price:.2f}")

    def book_table(self, num_table):
        if num_table not in self.booked_tables: 
            self.booked_tables.append(num_table)
            print(f"Table {num_table} has been reserved.")
        else:
            print(f"Table {num_table} is already booked.")

    def customer_order(self, customer_name, order_items):
        order = {
            'customer_name': customer_name,
            'order_items': order_items
        }
        self.customer_orders.append(order)
        print(f"Order for {customer_name} has been taken.")

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price:.2f}")

    def print_table_reservations(self):
        print("Table Reservations:")
        if not self.booked_tables:
            print("No tables reserved.")
        else:
            for table in self.booked_tables:
                print(f"Table {table} is reserved.")

    def print_customer_orders(self):
        print("Customer Orders:")
        if not self.customer_orders:
            print("No orders placed.")
        else:
            for order in self.customer_orders:
                print(f"Customer: {order['customer_name']}")
                print("Order Items:")
                for item in order['order_items']:
                    print(f"  - {item}")
                print()


restaurant1 = Restaurant()


restaurant1.add_menu_items("Burger", 5.99)
restaurant1.add_menu_items("Pizza", 8.99)
restaurant1.add_menu_items("Pasta", 7.49)

restaurant1.book_table(1)  
restaurant1.book_table(2)
restaurant1.book_table(3)

restaurant1.customer_order("Layyana", ["Burger", "Pasta"])
restaurant1.customer_order("Junaid", ["Pizza"])

restaurant1.print_menu()

restaurant1.print_table_reservations()

restaurant1.print_customer_orders()
