import datetime
import csv
from Package import Package
from HashTable import HashTable

# B2: My program exchanges data from WGUPS Package File.csv to my computer that runs the application (Host
# environment by assigning variables to the corresponding column cell in each row. My application then takes these
# variables and creates a Package object that will be added to the corresponding truck. This process of exchanging data
# from the WGUPS Package CSV file to my computer that runs my application continues until the entire CSV file has been
# read and each package has been loaded onto a truck
with open('/Users/spenc/Desktop/NHP1/WGUPS Package File.csv', mode='r') as csv_file:    # Open package file
    table = HashTable()  # Creating HashTable object
    fixed_address = '410 S State St'

    # D/D1: An array (truck_one - truck_three) that stores package IDs will perform well with my algorithm because it
    # will be iterated through checking each package's distance to determine the shortest distance from the truck's
    # current location. The array accounts for the relationship between the data points by accessing the correct data
    # (package address, and distance) by using the Package IDs that are stored in the array

    truck_one = []  # Creating 3 trucks to be loaded up
    truck_two = []
    truck_three = []
    delivery_ti = datetime.time(hour=14, minute=30, second=30)  # Creating Datetime placeholder object
    packages = [line.split(',') for line in csv_file]
    for i, x in enumerate(packages):

        if x[0] in (None, ""):  # For each line in the package file: if empty read line
            csv_file.readline()

        else:
            # Assigning package variables from the WGUPS Package File
            pac_id = int(x[0].strip())
            address = x[1].strip()
            city = x[2].strip()
            zip_code = x[4].strip()
            deadline = x[5].strip()
            weight = int(x[6])
            notes = x[7].strip()

            # Instantiate Package object using variables assigned from the CSV file
            package = Package(pac_id, address, city, zip_code, deadline, weight, notes,
                              "In hub", delivery_ti)

            key = package.id()  # Create key for Hash Table using package ID
            table.insert(key, package)  # Insert Package object into Hash Table

            if pac_id == 19:    # Determining package ID that must be Delivered with 14 & 16
                truck_one.append(package.id())

            elif 'Wrong address listed' in package.notes():  # Fixing wrong address and appending to truck 3
                package.address(fixed_address)
                truck_three.append(package.id())

            elif 'Can only be on truck' in package.notes() or 'Delayed on' in package.notes():  # Loading up truck_two
                truck_two.append(package.id())

            elif 'EOD' != package.deadline():   # Loading up truck_one
                truck_one.append(package.id())

            elif len(truck_three) < 16:  # Loading up truck_three
                truck_three.append(package.id())

            elif len(truck_two) < 16:   # Loading up remaining packages on truck_two
                truck_two.append(package.id())

            elif len(truck_one) < 16:   # Loading up remaining packages on truck_one
                truck_one.append(package.id())

print('truck_one contains:', len(truck_one))
print('truck_two contains:', len(truck_two))
print('Truck_three contains:', len(truck_three))

# This function is designed to take in a package_ID and return the respective address
def get_p_address(id_value):    # Complexity: O(1)
    item = table.get(id_value)
    return item.address()

# This function is designed to update the package delivery time variable given the ID and the updated time
def set_time(id_value, d_time):     # Complexity(1)
    item = table.get(id_value)
    item.delivery_time(d_time)

def get_hash_table():   # Getter Function for Hash Table; Complexity: O(1)
    return table

def get_truck_one():    # Getter Function for truck_one; Complexity: O(1)
    return truck_one

def get_truck_two():    # Getter Function for truck_two; Complexity: O(1)
    return truck_two

def get_truck_three():    # Getter Function for truck_three; Complexity: O(1)
    return truck_three

# This function is designed to print package variables by finding a Package specified by an ID and return the package
# information
def findPackage(id_value):  # Complexity: O(1)
    item = table.get(id_value)  # Getting package object from the HashTable using getter function
    print('Package ID is:', item.id())
    print('Package Address is:', item.address())
    print('Package City is:', item.city())
    print('Package Deadline is:', item.deadline())
    print('Package Zip is:', item.zip())
    print('Package Weight is:', item.weight())
    print('Package Notes are:', item.notes())
    print('Package Status is:', item.status())
    print('Package Delivery Time is:', item.delivery_time())

# This function is designed to print the package status of every package by taking in a user requested time and deliver
# each package ID & status in the Hash Table
def packageStatus(user_time):   # Complexity: O(n)
    for package_id in range(1, 41):
        current_package = table.get(package_id)
        package_time = current_package.delivery_time()

        if package_time >= user_time:  # Print Packages that are In Transit
            current_package.status('In Transit')
            print('Package ID:', current_package.id())
            print('Package Status:', current_package.status())

        else:  # Print Packages that are "Delivered"
            current_package.status('Delivered')
            print('Package ID:', current_package.id())
            print('Package Status:', current_package.status())

