# Spencer Koss
# SID: 000932676

import datetime
import time
import csv
from Package import Package
from HashTable import HashTable
from csv_package_file import *
from csv_distance_table import *

# This function is designed to provide a human-readable CLI for the user
def mainMenu():  # Complexity: O(1)
    print('Welcome to WGUPS!')
    print('Please enter the Number which you would like to select:')
    print('1. Package Information')
    print('2. Insert a Time and retrieve all Package Information')
    print('3. Exit WGUPS Postal Service Program')
    user_input = int(input())

    if user_input == 1:  # If user selects 1 then determine which package they would like to find
        package_value = int(input('Please Enter Package ID value:'))
        findPackage(package_value)
        userStatus()

    elif user_input == 2:   # If user selects 2 then print all package ID & status determined by user inputted time
        h, m, s = input("Enter a time to check delivery status (HH MM SS 24-Hour Cycle): ").split()
        user_time = datetime.time(hour=int(h), minute=int(m), second=int(s))
        packageStatus(user_time)
        userStatus()

    elif user_input == 3:   # If user selects 3 then exit program
        exit()

# This function is designed to determine if the user would like to return to the Main Menu
def userStatus():   # Complexity: O(1)
    user_status = str(input('Press Y to return to Main Menu and anything else to Exit \n'))
    user_status = user_status.upper()
    if user_status == 'Y':
        mainMenu()

# B4: The nearest neighbor algorithm can adapt to handle a growing amount of work for either packages and/or amount of
# trucks. As the amount of packages increase, the distance 2-D list and dictionary have the ability to scale to the
# requested amount. This solution has the ability to scale because it delivers each package by determining the shortest
# distance until the truck is empty. This works with a growing amount of work because it can be used for any amount
# of trucks or bigger trucks than can store more packages

# B5: This software is efficient because the nearest neighbor algorithm delivers all packages under 140 miles.
# This solution is easy to maintain because it provides the ability to deliver all of the packages for each and every
# truck that is passed in regardless of amount of packages or amount of trucks. This allows for this software to not
# only be efficient in delivering the packages on time(or earlier), but due to the implementation it is easy to maintain

# truck_route has 2 parameters: truck, and a start time for when the truck dispatches, leaving the hub
# The while loop iterates through the truck's packages passing in the three parameters needed to determine and deliver
# a package: truck, location, and a time (updated when the previous packaged was delivered)
# Once all of the packages have been delivered this function adds the mileage from the trucks current location back to
# The hub and returns the total miles for that specific truck
def truck_route(truck, start_time):  # Complexity: O(n^2) since it uses while loop and nearest_neighbor function
    miles = 0.0
    current_loc = 0
    t_miles = 0.0

    # While truck's contents are not empty, deliver each package with the shortest distance and calculate total mileage
    while len(truck) > 0:
        current_loc, miles, start_time = nearest_neighbor(truck, current_loc, start_time)
        t_miles += miles

    if len(truck) == 0:     # All packages are delivered; add distance back to the hub
        miles = distance_list[current_loc][0]
        t_miles += miles

    return t_miles  # return total mileage for the specified truck

# This function is designed to get the 3 loaded trucks, deliver, and calculate the total mileage of all 3 trucks
def deliver_trucks():   # Complexity O(n^2) since it uses truck_route & nearest_neighbor algorithm
    total_miles = 0
    truck_1 = get_truck_one()   # Get 3 trucks loaded up with packages
    truck_2 = get_truck_two()
    truck_3 = get_truck_three()

    t1_time = datetime.time(hour=int(8), minute=int(0), second=int(0))  # Creating 3 Start Times for each truck
    t2_time = datetime.time(hour=int(9), minute=int(10), second=int(0))
    t3_time = datetime.time(hour=int(10), minute=int(0), second=int(0))

    total_miles = truck_route(truck_1, t1_time)     # Calculate total mileage
    total_miles += truck_route(truck_2, t2_time)
    total_miles += truck_route(truck_3, t3_time)
    print('Total miles for all 3 trucks delivered:', total_miles, '\n')

class Main:
    deliver_trucks()
    mainMenu()

