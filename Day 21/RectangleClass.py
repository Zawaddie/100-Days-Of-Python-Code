# understanding of creating a class, 
# defining attributes and methods,
#using objects to perform calculations based on the defined class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)

# Create an object of the Rectangle class
rectangle1 = Rectangle(5, 10)

# Calculate and print the area of the rectangle
area = rectangle1.get_area()
print("Area:", area)

# Calculate and print the perimeter of the rectangle
perimeter = rectangle1.get_perimeter()
print("Perimeter:", perimeter)
