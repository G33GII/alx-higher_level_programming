class Square:
    """
    Class that defines properties of a square (based on 3-square.py).

    Attributes:
        __size: Size of a square (1 side).
    """

    def __init__(self, size=0):
        """Creates new instances of a square.

        Args:
            size (int): Size of the square (1 side). Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): Size of the square (1 side).
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
