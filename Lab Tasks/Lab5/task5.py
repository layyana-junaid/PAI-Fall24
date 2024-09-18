# Layyana Junaid 23k-0056 BSAI_3A
# Task 5

class Vehicle:
    def __init__(self, model, make, rental_price):
        self.model = model
        self.make = make
        self.rental_price = rental_price
        self.is_available = True  

    def check_availability(self):
        return self.is_available

    def calculate_rental_cost(self, days):
        return self.rental_price * days

    def display_details(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Rental Price: ${self.rental_price:.2f}")
class Car(Vehicle):
    def __init__(self, make, model, rental_price, num_doors, fuel_type):
        super().__init__(make, model, rental_price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type

    def display_details(self):
        super().display_details() 
        print(f"Number of Doors: {self.num_doors}")
        print(f"Fuel Type: {self.fuel_type}")

class SUV(Vehicle):
    def __init__(self, make, model, rental_price, seating_capacity):
        super().__init__(make, model, rental_price)
        self.seating_capacity = seating_capacity

    def display_details(self): 
        super().display_details()  
        print(f"Seating Capacity: {self.seating_capacity}")

class Truck(Vehicle):
    def __init__(self, make, model, rental_price, payload_capacity):
        super().__init__(make, model, rental_price)
        self.payload_capacity = payload_capacity

    def display_details(self): 
        super().display_details()  
        print(f"Payload Capacity: {self.payload_capacity}")

class RentalReservation:
    def __init__(self, customer_id, vehicle_id, start_date, end_date):
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date

    def create_reservation(self): 
        pass

    def cancel_reservation(self):
        pass

    def calculate_total_cost(self):
        pass

class Customer:
    def __init__(self, customer_id, name, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def display_rental_history(self):
        for rental in self.rental_history:
            print(rental) 

customer1 = Customer(1, "Layyana Junaid", "layyana@example.com")
car1 = Car("Toyota", "Camry", 50.00, 4, "Gasoline")
reservation1 = RentalReservation(customer1.customer_id, car1.model, "2023-09-20", "2023-09-23")
reservation1.create_reservation() 

customer1.rental_history.append(reservation1)
customer1.display_rental_history()  

car1.display_details() 