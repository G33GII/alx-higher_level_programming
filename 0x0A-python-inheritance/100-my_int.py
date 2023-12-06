class MyInt(int):
    """
    A class that inherits from 'int' and alters comparison methods.
    
    This class modifies the behavior of the equality (__eq__) and inequality (__ne__)
    comparison methods to swap their functionality.
    """

    def __eq__(self, other):
        """
        Override the equality (==) comparison method.
        
        Args:
            other: Another object to compare against.

        Returns:
            bool: True if this object is not equal to 'other', False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality (!=) comparison method.
        
        Args:
            other: Another object to compare against.

        Returns:
            bool: True if this object is equal to 'other', False otherwise.
        """
        return super().__eq__(other)
