"""
This program is to caclculate the fuel needed to launch the modules
"""
# Retrieving data.
with open('Day_One/modules.txt', 'r') as file:
    content = file.readlines()

# Striping line breaks
content = [int(x.strip()) for x in content]

# Getting total of fuel needed per module
get_fuel_amount = [con//3-2 for con in content]

# Printing the sum of the fuel of all the modules
if __name__ == "__main__":
    print(f'The fuel required to launch all the modules is {sum(get_fuel_amount)}.')
