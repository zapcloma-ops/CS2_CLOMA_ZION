# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

if not name.strip():
  print("ERROR: Invalid name. Please enter a name.)
if distance <= 0:
  print("ERROR: Invalid value. Enter a number greater than 0.")
if passengers <= 0:
  print("ERROR: Invalid value, Enter a whole number value.")

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
