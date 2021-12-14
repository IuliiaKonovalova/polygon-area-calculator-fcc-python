class Rectangle:
    """
    Consist following methods: set_width, set_height, get_area,
    get_perimeter, get_diagonal, get_picture, get_amount_inside
    """
    def __init__(self, width, height):
        """
        Initialize with width and height attributes
        """
        self.width = width
        self.height = height

    def set_width(self, width):
        """
        Sets width
        """
        self.width = width

    def set_height(self, height):
        """
        Sets height
        """
        self.height = height

    def get_area(self):
        """
        Returns area by multiplying width by height
        """
        area = self.width * self.height
        return area

    def get_perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        """
        Returns the diagonal of the rectangle
        """
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        """
        Returns a picture of the rectangle, if the width and height is < 50
        If height or/and width is > 50, it returns: "Too big for picture."
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
        else:
            picture = ("*" * self.width + "\n") * self.height
            return picture

    def get_amount_inside(self, shape):
        """
        checks how many given shapes could fit into initial shape
        """
        return int(self.get_area()/shape.get_area())

def __str__ (self):
    return f'Rectangle(width={self.width}, height={self.height})'



# class Square:
