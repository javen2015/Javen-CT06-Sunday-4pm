# Simple Python program to calculate bus fare in Singapore

# Ask user for distance travelled and if they took an express bus
distance = float(input("How far did you travel? (in km): "))
express_bus = input("Did you take an express bus? (yes/no): ")

# Start with the first 3.2 km costing $0.99
total_fare = 0.99
remaining_distance = distance - 3.2

# Add fares based on distance travelled
if remaining_distance > 0:
    next_distance = min(remaining_distance, 3.0)
    total_fare += next_distance * 0.10
    remaining_distance -= next_distance

if remaining_distance > 0:
    next_distance = min(remaining_distance, 3.0)
    total_fare += next_distance * 0.08
    remaining_distance -= next_distance

if remaining_distance > 0:
    next_distance = min(remaining_distance, 10.0)
    total_fare += next_distance * 0.04
    remaining_distance -= next_distance

if remaining_distance > 0:
    next_distance = min(remaining_distance, 4.0)
    total_fare += next_distance * 0.03
    remaining_distance -= next_distance

if remaining_distance > 0:
    next_distance = min(remaining_distance, 3.0)
    total_fare += next_distance * 0.02
    remaining_distance -= next_distance

if remaining_distance > 0:
    next_distance = min(remaining_distance, 14.0)
    total_fare += next_distance * 0.01
    remaining_distance -= next_distance

if remaining_distance > 0:
    total_fare += remaining_distance * 0.01

# Add $0.60 if express bus is taken
if express_bus.lower() == 'yes':
    total_fare += 0.60

# Show the final fare rounded to 2 decimal places
print("Your bus fare is: $" + str(round(total_fare, 2)))
