class Rectangle:
    number_of_instances = 0  # Class variable to track the number of instances

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1  # Increment count on instance creation

    # Other methods...

    @classmethod
    def get_number_of_instances(cls):
        """Returns the current number of instances."""
        return cls.number_of_instances

# Example usage:
print(Rectangle.get_number_of_instances())  # Output: 0

rect1 = Rectangle(5, 10)
print(Rectangle.get_number_of_instances())  # Output: 1

rect2 = Rectangle(3, 7)
print(Rectangle.get_number_of_instances())  # Output: 2

# Additional instances can be created and the count will increase accordingly
