import csv
import datetime
import Package
import HashTable
from csv_package_file import *

# B2: My program exchanges data from WGUPS Distances.csv to my computer that runs my application by assigning each value
# in the Distances.csv file to a 2 Dimensional list called distances. This process will continue to exchange data
# from the WGUPS Distance.csv file to my computer that hosts my application until the entire CSV file has been read and
# loaded into the distances list. I create another 2-D list called distance_list that iterates through the distances
# (The 2-D list of strings) and converts each string value in the list to a float value in order to later determine
# the distance from the current location to the destination
with open('/Users/spenc/Desktop/NHP1/WGUPS Distances.csv', mode='r') as csv_file:

    # Create 2-D List populated with distance variables from the csv file in strings
    distances = list(csv.reader(csv_file, delimiter=','))

    # B6: My 2-D list (distance_list) has many strengths for this scenario, including access time. For python, lists
    # have an complexity of O(1) when accessed by index with row and column. This plays a key role in running time
    # because I am able to access this 2-D list efficiently. The weakness from using a 2-D list is that it has no
    # encryption like a Hash Table would have from generating a hashed value from the key.

    # Now I create a 2-D List that converts the strings from the CSV file to float values
    distance_list = [[float(string) for string in inner] for inner in distances]

# B2: My program exchanges data from the WGUPS addresses.csv file to my computer that hosts the application by first
# creating an empty Dictionary called addresses and reads through each line of the CSV file assigning its key as the
# (string) address and its associated integer value to the value. This data exchange process from reading in the CSV
# file to my computer that hosts my application and stores the associated address and integer value to the dictionary
# will continue until the entire CSV file has been read
with open('/Users/spenc/Desktop/NHP1/WGUPS addresses.csv', mode='r') as csv_file_2:
    reader = csv.reader(csv_file_2)
    col = 0  # Creating a column integer value to later navigate through distances list

    # B6: My Dictionary (addresses) also has many strengths for this scenario. The importance for using a dictionary in
    # this scenario is to have efficient access time. A dictionaries get() function has a complexity of O(1) making a
    # dictionary effective for this implementation. A weakness that dictionaries have is that eventually as the
    # dictionary becomes larger and larger, it can be considered "full" where collisions can occur and this can
    # negatively impact performance. This implementation of a dictionary is efficient and I don't need to consider
    # collisions, but as the number of addresses increases then it can lead to performance loss due to access time
    # from collisions

    addresses = {}  # Creating an empty Dictionary
    for row in reader:
        address = row[1].replace('\n', ' ').strip()  # Get address variable replacing any new lines and spacing
        addresses[address] = col    # insert key value pair in addresses dictionary to address (key) and col (int value)
        col += 1

# This function is designed to calculate the the delivery time using the distance of the package and the previous
# delivery time
def delivery_time(distance, start_time):    # Complexity: O(1)
    h = start_time.hour
    m = start_time.minute
    s = 0
    time = (distance / 18) * 60    # Calculating time in minutes using the trucks MPH
    m += time    # Adding existing minutes passed in
    hour, time = divmod(m, 60)
    h += int(hour)   # Incrementing new hours into existing hours
    m = int(time)
    f_time = datetime.time(hour=int(h), minute=int(m), second=int(s))
    return f_time

# The algorithm below is a greedy algorithm because it recursively looks for the best optimal destination (Shortest
# distance) at the current location.
# This function sets an upper-bound variable in order to determine the shortest distance by looping through the truck's
# current packages by updating the appropriate values if the package has a shorter distance
# Once the algorithm has determined the package with the shortest distance, it sets the delivery time, updates the truck
# to its current location, and removes the package_id from the truck's list

def nearest_neighbor(truck, curr_location, start_time):  # Complexity O(n)
    closest_neighbor = 30.2  # Setting upper-bound (As list iterates this number will change)
    i = 0
    while i < len(truck):
        pac_address = get_p_address(truck[i])  # Get package address given ID
        destination = addresses.get(pac_address)  # Get column Integer value given address
        distance = distance_list[curr_location][destination]    # Get distance using location and destination variables

        if distance < closest_neighbor:  # Checks if the number of miles is lower than the current lowest mileage
            closest_neighbor = distance
            delivery_id = truck[i]
            delivery_distance = distance
            loc = destination
            pac_time = delivery_time(distance, start_time)
        i += 1

    set_time(delivery_id, pac_time)  # Set Package delivery time
    start_time = pac_time   # update start_time to most recent package delivery time
    curr_location = loc  # Update the truck's current location
    truck.remove(delivery_id)   # Remove package ID from truck's list
    return curr_location, delivery_distance, start_time

