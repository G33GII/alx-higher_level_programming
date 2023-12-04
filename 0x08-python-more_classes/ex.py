class Rectangle:
    number = 0  # Class variable to track the number of instances

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number += 1  # Increment count on instance creation

    # Other methods...

    @classmethod
    def get_number_of_instances(cls):
        """Returns the current number of instances."""
        return cls.number

    number_of_instances = property(get_number_of_instances)  # Make it accessible directly

# Example usage:
print(Rectangle.number_of_instances)  # Output will show the current number of instances
