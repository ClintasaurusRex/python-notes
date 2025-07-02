# Write a program that:

# Takes a number as input from the user (float).
# Takes the number of decimal places to round to (integer).
# Outputs the rounded number.

num = float(input())
decimal_places = int(input())
rounded = round(num, decimal_places)
print(rounded)

