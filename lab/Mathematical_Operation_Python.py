#Adition

from cgi import print_form


answer= 25+25
print(f"result: {answer}")

#Subtraction
difference= 30-23
print(f"result: {difference}")

#Multiplication
product = 30 * 12
print(f"result: {product}")


#Division
quotient = 28 / 12
print(f"result: {quotient}")

#convert

seconds = 1040
display_minutes = seconds // 60
print(f"minutos: {display_minutes}")

#add module
seconds1 = 1040
display_minutes1 = seconds1 // 60
display_seconds = seconds1 % 60

print(display_minutes1)
print(display_seconds)

#Order of Operation
result_1 = 1050 + 26 * 2
result_2 = 1050 + (26 * 2)

print(f"result: {result_1}")
print(f"result: {result_2}")


#USE ARITHMETIC OPERATORS
first_planet = 149597870
second_planet = 778547200
distance_km = second_planet - first_planet
print(f"distance_km: {distance_km}")

distance_mi = distance_km / 1.609344
print(f"distance_mi: {distance_mi}")

# WORK WITH NUMBERS IN PYTHON
# convert strings to numbers
demo_int = int('215')
print(f"demo_int: {demo_int}" )

demo_float = float('215.3')
print(f"demo_float: {demo_float}")

#ABS
print("abs")
print(abs(39 - 16))
print(abs(16 - 39))
#ROUNDING
print("rounding")
print(round(15.5))

#using library
print("library")

from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)


#Using advanced opeartions
first_planet_input = int(input('Enter the distance from the sun for the first planet in KM: '))
second_planet_input = int(input('Enter the distance from the sun for the second planet in KM: '))
distance_km1 = second_planet_input - first_planet_input
print(f"the distance is: {abs(distance_km1)}")
