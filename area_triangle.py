# Program to find the area of a triangle whose base and height is given.
base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
print("Area of triangle : ", 0.5 * base * height)

#Program to find the area of a triangle whose 3 sides are given.
import math
side1 = int(input("Enter the side A of the triangle: "))
side2 = int(input("Enter the side B of the triangle: "))
side3 = int(input("Enter the side C of the triangle: "))
side = (side1+side2+side3) / 2
print("Area of triangle with 3 sides given :", math.sqrt(side*(side-side1)*(side-side2)*(side-side3)))

#Program to find the area of an equilateral triangle.
side = int(input("Enter the side of the triangle:"))
print("Area of equilateral triangle :", math.sqrt(3/2)*(side**2))