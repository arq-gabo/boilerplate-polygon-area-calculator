class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def __str__(self):
        return self.__class__.__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"
         
    def get_picture(self):
        output = ""
        if self.width > 50 or self.height > 50:
            output = "Too big for picture."
        else:
            for _ in range(self.height):
                output += "*" * self.width + "\n"

        return output
    
    def get_amount_inside(self, rec_or_sq):
        return (self.width // rec_or_sq.width) * (self.height // rec_or_sq.height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def set_side(self, new_side):
        super().set_height(new_side)
        super().set_width(new_side)

    def set_width(self, new_width):
        self.set_side(new_width)

    def set_height(self, new_height):
        self.set_side(new_height)

    def __str__(self):
        return self.__class__.__name__ + "(side=" + str(self.width) + ")"