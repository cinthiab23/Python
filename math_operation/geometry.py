def rectangle(length, width):
    area = length * width
    print("The area of the rectangle is" + str(area))


def triangle(base, height):
    area = 0.5 * base * height
    print("The area of the triangle is" + str(area))


def circle(radius):
    pi = 3.14
    area = pi * radius * radius
    print("The area of the circle is" + str(area))


def main():
    # User input for rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle(length, width)

    # User input for triangle
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    triangle(base, height)

    # User input for circle
    radius = float(input("Enter the radius of the circle: "))
    circle(radius)


main()
