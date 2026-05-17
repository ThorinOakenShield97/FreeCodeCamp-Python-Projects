** start of main.py **

class Rectangle:
    """
    A class used to represent a Rectangle and perform geometric calculations.
    """
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        """Sets the width of the rectangle."""
        self.width = width
    
    def set_height(self, height: int) -> None:
        """Sets the height of the rectangle."""
        self.height = height
    
    def get_area(self) -> int:
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        """Calculates and returns the perimeter of the rectangle."""
        return (self.width + self.height) * 2
    
    def get_diagonal(self) -> float:
        """Calculates and returns the diagonal length of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self) -> str:
        """
        Returns a string representation of the shape using lines of '*'.
        Returns a specific message if the width or height is greater than 50.
        """
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        
        # String multiplication to build the shape visualization
        return (self.width * '*' + '\n') * self.height
    
    def get_amount_inside(self, shape: "Rectangle") -> int:
        """
        Calculates how many times the passed shape could fit inside the 
        current shape (without rotations).
        """
        # Integer division (//) calculates the exact fit along each axis
        n_width = self.width // shape.width
        n_height = self.height // shape.height
        return n_width * n_height
    
    def __str__(self) -> str:
        """Returns the string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """
    A subclass of Rectangle used to represent a Square.
    Inherits all methods from Rectangle but maintains equal width and height.
    """
    def __init__(self, side: int) -> None:
        # Calls the parent (Rectangle) constructor with equal width and height
        super().__init__(side, side)

    def set_side(self, side: int) -> None:
        """Sets the side of the square (updates both width and height)."""
        self.width = side
        self.height = side

    def set_width(self, width: int) -> None:
        """Overrides set_width to ensure width and height remain equal (DRY principle)."""
        self.set_side(width)
    
    def set_height(self, height: int) -> None:
        """Overrides set_height to ensure width and height remain equal (DRY principle)."""
        self.set_side(height)
    
    def __str__(self) -> str:
        """Returns the string representation of the square."""
        return f"Square(side={self.width})"


# --- Testing block ---
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print("--- Rectangle Tests ---")
    print("Area:", rect.get_area())
    rect.set_height(3)
    print("Perimeter:", rect.get_perimeter())
    print(rect)
    print("Picture:")
    print(rect.get_picture(), end="")

    sq = Square(9)
    print("\n--- Square Tests ---")
    print("Area:", sq.get_area())
    sq.set_side(4)
    print("Diagonal:", sq.get_diagonal())
    print(sq)
    print("Picture:")
    print(sq.get_picture(), end="")

    rect.set_height(8)
    rect.set_width(16)
    print("\n--- Amount Inside Test ---")
    print(f"How many Squares(side=4) fit in Rectangle(width=16, height=8)?")
    print("Result:", rect.get_amount_inside(sq))


** end of main.py **

