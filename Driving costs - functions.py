#function
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    gallons_used = miles_driven / miles_per_gallon
    cost = gallons_used * dollars_per_gallon
    return cost
    return cost

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):}')
print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):}')
print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):}')