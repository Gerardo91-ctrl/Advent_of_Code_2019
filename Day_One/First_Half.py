with open('Day_One/modules.txt', 'r') as file:
    content = file.readlines()


content = [int(x.strip()) for x in content]

get_fuel_amount = sum([con//3-2 for con in content])

print(get_fuel_amount)