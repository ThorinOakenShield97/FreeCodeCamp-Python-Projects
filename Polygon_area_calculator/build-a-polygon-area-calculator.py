** start of main.py **

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width:int):
        self.width = width
    
    def set_height(self,height:int):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width + self.height) * 2
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        return (self.width * '*' + '\n') * self.height
    
    def get_amount_inside(self,shape):
        n_width = self.width // shape.width
        n_height = self.height // shape.height
        return n_width * n_height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def set_width(self,width):
        self.height = width
        self.width = width
    
    def set_height(self,height):
        self.width = height
        self.height = height
    
    def set_side(self,side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.width})"

# Usage examples:

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))


** end of main.py **

