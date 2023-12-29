import csv
class Driver():
    def __init__(self, name, number, location, num_seats):
        self.name = name
        self.number = number
        if location == "Dinky" or location == "Como":
            location = "Dinky/Como"
        elif location == "Stadium Village" or location == "Superblock":
            location = "Stadium Village/Superblock"
        self.location = location

        self.num_seats = num_seats
        self.carpool = []

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_location(self):
        return self.location

    def get_num_taken_seats(self):
        return len(self.carpool)

    def get_num_seats(self):
        return self.num_seats

    def has_seats_left(self):
        if self.get_num_taken_seats() < self.get_num_seats():
            return True
        else:
            return False

    def add_to_carpool(self, rider):
        self.carpool.append(rider)

    def show_carpool(self):
        print(self.get_name(), "(", self.get_number(), ")", "'s carpool leaving from ", self.location, " has:")
        for i in range(len(self.carpool)):
            print("*", self.carpool[i].get_name(), " - ", self.carpool[i].get_number())


class Rider():
    def __init__(self, name, number, location):
        self.name = name
        self.number = number
        if location == "Dinky" or location == "Como":
            location = "Dinky/Como"
        elif location == "Stadium Village" or location == "Superblock":
            location = "Stadium Village/Superblock"
        self.location = location

    def get_location(self):
        return self.location

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def show_rider_info(self):
        print(" - ", self.get_name(), "from ", self.get_location())

with open("Nov_10_data", mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    rows = list(csv_reader)  # Read the rows into a list for multiple iterations


print("All the data")
for row in rows:
    print(row)

print("Row 4")
for row in rows:
    if len(row) > 4:  # Check if the row has enough elements
        print(row[4])

all_riders = []
all_drivers = []
girls_without_rides = []

print("Seeing who can be a driver")
# Sort the girls into drivers and riders.
for row in rows:
    if len(row) > 5 and row[4] == "Yes":  # Check if the row has enough elements
        print("Creating a new driver")
        # Create a new Driver
        driver = Driver(row[1], row[2], row[3], int(row[5]))  # Name, location, num seats
        all_drivers.append(driver)
    elif len(row) > 3:
        print("Creating a rider")
        rider = Rider(row[1], row[2], row[3])
        all_riders.append(rider)

# Try to place the riders into carpools.
for rider in all_riders:
   carpool_found = False
   for driver in all_drivers:
       if (rider.get_location() == driver.get_location()) and (driver.has_seats_left()):
           driver.add_to_carpool(rider)
           carpool_found = True
           break  # move onto the next rider
   if not carpool_found:
       girls_without_rides.append(rider)


drivers_with_seats_left = []


# Find out if any carpools have extra spots
for driver in all_drivers:
   if driver.has_seats_left():
       drivers_with_seats_left.append(driver)


# Output all the results.
print("\nThe carpools: ")
for driver in all_drivers:
    driver.show_carpool()

print("\nGirls without rides")
for rider in girls_without_rides:
    rider.show_rider_info()

print()
if len(drivers_with_seats_left) == 0:
    print("There are no drivers with spots left :(")
else:
    print("Drivers with spots left")
    for driver in drivers_with_seats_left:
        driver.show_carpool()  # Correct method call
