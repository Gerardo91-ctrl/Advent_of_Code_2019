"""
This programs is to calculate the extra fuel needed to launch the modules with their respective fuels.
"""
# Get the modules from modules.txt
with open('Day_One/modules.txt', 'r') as file:
    content = file.readlines()

# Striping the line breaks
content = [int(x.strip()) for x in content]

# Calculate fuel requirements for each module.


def get_fuel_module(module_mass):
    return module_mass // 3 - 2


modules_fuel = [get_fuel_module(module_mass)
                for module_mass in content]
print(modules_fuel)
# Caculate the fuel needed for the fuel
# mass of each module


def get_fuel_fuel(fuel_mass):
    if fuel_mass <= 0:
        return 0
    else:
        return fuel_mass + get_fuel_fuel(fuel_mass//3-2)


fuel_fuel = [get_fuel_fuel(fuel_mass) for fuel_mass
             in modules_fuel]

# Print answer
if __name__ == "__main__":
    print(sum(fuel_fuel))
