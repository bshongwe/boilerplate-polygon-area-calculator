class Rectangle:
    """A class to represent a rectangle."""

    def __init__(self, width: int, height: int):
        """Initializes a new Rectangle object."""
        self.width = width
        self.height = height

    def set_width(self, width: int):
        """Sets the width of the rectangle."""
        self.width = width

    def set_height(self, height: int):
        """Sets the height of the rectangle."""
        self.height = height

    def get_area(self) -> int:
        """Returns the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self) -> int:
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        """Returns the diagonal of the rectangle."""
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self) -> str:
        """Returns a string that represents the shape using lines of "*".

        If the width or height is larger than 50, this should return the string:
        "Too big for picture.".
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += "\n"

        return picture

    def get_amount_inside(self, shape: Rectangle) -> int:
        """Takes another shape (square or rectangle) as an argument.

        Returns the number of times the passed in shape could fit inside the shape
        (with no rotations).
        """
        return self.width // shape.width * self.height // shape.height

    def __str__(self) -> str:
        """Returns a string representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """A class to represent a square."""

    def __init__(self, side: int):
        """Initializes a new Square object."""
        super().__init__(side, side)

    def set_side(self, side: int):
        """Sets the side length of the square."""
        self.width = side
        self.height = side

    def __str__(self) -> str:
        """Returns a string representation of the square."""
        return f"Square(side={self.width})"


# Example usage:

rectangle = Rectangle(5, 10)
print(rectangle.get_area())  # 50
print(rectangle.get_perimeter())  # 30
print(rectangle.get_diagonal())  # 11.180339887498949
print(rectangle.get_picture())
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *

square = Square(9)
print(square.get_area())  # 81
print(square.get_perimeter())  # 36
print(square.get_diagonal())  # 12.727922061357856
print(square.get_picture())
# ********
# ********
# ********
# ********
# ********
# ********
# ********
# ********
# ********

# Get the amount of squares that can fit inside the rectangle.
print(rectangle.get_amount_inside(square))  # 9
