#Layyana Junaid 23k-0056
#Lab 4 task 7

class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare_calculation(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, seating_capacity):
          super().__init__(seating_capacity) #calls the innit function or constructor of parent class

    def calculate_fare(self, seating_capacity):
        fare = super().fare_calculation()
        maintenance_charge = 0.10 * fare
        total_fare = fare + maintenance_charge
        return total_fare

bus = Bus(seating_capacity=50)
print(f"The fare for the bus is ${bus.fare_calculation():.2f}")


