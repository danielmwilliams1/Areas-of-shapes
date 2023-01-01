## area of circle

import math

def area_shapes(radius):
    area = math.pi * radius ** 2
    return area

def main():
    radius = float(input("Enter radius: "))
    print("Area of circle is", area_shapes(radius))

main()

# Path: area_rectangle.py
## area of rectangle

def area_rectangle(length, width):
    area = length * width
    return area

def main():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of rectangle is", area_rectangle(length, width))
    
main()

# Path: area_triangle.py

def area_triangle(base, height):
    area = 0.5 * base * height
    return area

def main():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle is", area_triangle(base, height))
    
main()

# Path: area_square.py

def area_square(side):
    area = side ** 2
    return area

def main():
    side = float(input("Enter side: "))
    print("Area of square is", area_square(side))

main()

# Path: area_parallelogram.py

def area_parallelogram(base, height):
    area = base * height
    return area

def main():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of parallelogram is", area_parallelogram(base, height))
    
main()

# Path: area_trapezoid.py

def area_trapezoid(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

def main():
    base1 = float(input("Enter base1: "))
    base2 = float(input("Enter base2: "))
    height = float(input("Enter height: "))
    print("Area of trapezoid is", area_trapezoid(base1, base2, height))
    
main()

