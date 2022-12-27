print("\n\n*  *  *  WELCOME  *  *  *")
print("CALCULATE YOUR DRIVING COST\n")

fuel_price = float(input("Enter fuel price (PLN): ").replace(',', '.'))
average_fuel_consumption = float(input("Average fuel consumption (L/100km): ").replace(',', '.'))
route_length = float(input("Length of the route (km): ").replace(',', '.'))

cost = float((average_fuel_consumption / 100) * fuel_price) * route_length
driving_cost = str(round(cost, 2)).replace('.', ',')

# print(type(driving_cost))
print(f"\nDRIVING COST: {driving_cost} PLN")

input("\nPress Enter to Exit...")
