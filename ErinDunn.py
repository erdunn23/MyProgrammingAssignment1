# Erin Dunn
# CS151, Prof. Mehri
# 27 September 2021
# Programming Assignment: 1
# Program Inputs: length, width, and height dimensions of room in feet
# Program Outputs: total area in square feet, gallons of primer needed, gallons of paint needed

# this will be used later to round the gallons of paint and primer needed
import math

# dimensions of the room input required by user
length = input("Enter length of room in feet:")
width = input("Enter width of room in feet:")
height = input("Enter height of room in feet:")

# this declares those dimensions are floats (numbers with decimals), and not just a string
length = float(length)
width = float(width)
height = float(height)

# compute the area of the four walls
walls_area = length * height * 4
# compute the area of the ceiling
ceiling_area = length * width
# total area of the room (excluding the floor) is the sum of the area of the walls and the ceiling
total_area = walls_area + ceiling_area

# raw numbers of primer and paint needed are computed with float division according to amount of square feet covered per gallon
primer_needed = total_area / 200
paint_needed = total_area / 350

# these lines round the gallons of primer and paint needed
primer_needed = math.ceil(primer_needed)
paint_needed = math.ceil(paint_needed)

# program outputs the total area of the room, and number of gallons of primer and paint needed
print("Total area of room in square feet: ", total_area)
print("Gallons of primer needed: ", primer_needed)
print("Gallons of paint needed: ", paint_needed)