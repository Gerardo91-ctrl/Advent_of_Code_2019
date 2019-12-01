from First_Half import get_fuel_amount

my_fuel = get_fuel_amount
total_fuel = 0

while my_fuel > 0:
    my_fuel = my_fuel//3-2
    total_fuel = total_fuel + my_fuel


print(total_fuel + get_fuel_amount)