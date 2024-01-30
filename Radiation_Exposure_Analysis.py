'''
A simple program to practice using for loops and lists to input
radiation data and calculate the mean and standard deviation
in a set of locations
'''

from colorama import Fore
import statistics as st

# Initialise variables    
area = 0
locations = ["City Centre", "Industrial Zone", "Residential District", "Rural Outskirts", "Downtown"]
levels = [[22,19,20,31,28],[35,32,30,37,40],[15,12,18,20,14],[9,12,16,14,7],[25,18,22,21,26]]

# Print menu function - takes a list and loops through to print it
def print_menu(menu):
    print("\t----------------------")
    for i, item in enumerate(menu):
        print(f"\t  {Fore.LIGHTYELLOW_EX}{i+1}.{Fore.RESET} {item}")    
    print("\t----------------------")
    return

# Function to check that the menu selection is an integer and that it is in range
def menu_input_check(selection, menu_list):

    while True:
        if selection.isdigit() and int(selection) <= len(menu_list) and int(selection) > 0:
            break
        else:
            selection = input(f"\n{Fore.RED}[Invalid input]{Fore.RESET} Please select a number from the menu: ")

    return int(selection)

# Function to print the average and std deviation of the region. Takes a list index
def print_region_details(index):
    print("\n\nRegion details")
    print("----------------------")
    print(f"  Region:{Fore.LIGHTYELLOW_EX} {locations[index]} {Fore.RESET}")
    print(f"  Current radiation readings:{Fore.LIGHTYELLOW_EX} {levels[index]} {Fore.RESET}")
    print(f"  Average radiation level:{Fore.LIGHTYELLOW_EX} {calc_avg(levels[index]):.2f} {Fore.RESET}")
    print(f"  Standard deviation:{Fore.LIGHTYELLOW_EX} {st.stdev(levels[index]):.2f} {Fore.RESET}\n")


# Function to calculate the average, takes a list value
calc_avg = lambda list_items: sum(list_items)/len(list_items)

# print the intro to the program
print(f"\n================= {Fore.LIGHTYELLOW_EX}Radiation Analysis program{Fore.RESET} =================")
print("""This program will calculate the average radiation levels and
the standard deviation for the regions listed.""")

# print the menu and ask for a selection
print("\n\tRegion Menu")
print_menu(locations)
area = input("\nPlease select the region number from the menu: ")

# check for a valid menu input
area = menu_input_check(area, locations)

# Set area as index for list
area = area -1

# call the print region function using the menu index to get the right list values
print_region_details(area)

# check if new data should be added
new_levels = input("Would you like to add new radiation data [Y/N]? ")

if new_levels.lower() == 'y':
    while True:
        level = input("Enter radiation level or 'done' to finish: ")
        if level.lower() == "done":
            print_region_details(area)
            break
        try:
            levels[area].append(int(level))
        except ValueError:
            print("Invalid input,please enter a number.")

# end program
print(f"\n================= Program ended =================\n")

