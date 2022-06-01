class Polygon:
    def __init__(self, sides) -> None:
        self.sides = sides

    def area(self):
        pass

    def perimeter(self):
        pass

class Triangle(Polygon):
    def __init__(self, side1, side2, base, height) -> None:
        super().__init__(3)
        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height / 2
    
    def perimeter(self):
        return self.base + self.side1 + self.side2

class Quadrilateral(Polygon):
    def __init__(self, base, height, side1, side2, top) -> None:
        super().__init__(4)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.top = top
    
    def area(self):
        return self.base * self.height

    def perimeter(self):
        return self.base + self.side1 + self.side2 + self.top

class Pentagon(Polygon):
    def __init__(self, length) -> None:
        super().__init__(5)
        self.length = length
    
    def area(self):
        return ((25+500**0.5)**0.5)/4*self.length**2
    
    def perimeter(self):
        return 5*self.length

class Hexagon(Polygon):
    def __init__(self, length) -> None:
        super().__init__(6)
        self.length = length
    
    def area(self):
        return 27**0.5 / 2 * self.length**2
    
    def perimeter(self):
        return 6*self.length

class Octagon(Polygon):
    def __init__(self, length) -> None:
        super().__init__(8)
        self.length = length

    def area(self):
        return (2 + 8**0.5)*self.length**2
    
    def perimeter(self):
        return 8*self.length

class IsocelesTriangle(Triangle):
    def __init__(self, side, base, height) -> None:
        super().__init__(side1=side, side2=side, base=base, height=height)
    
    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()

class EqualateralTriangle(IsocelesTriangle):
    def __init__(self, length) -> None:
        height = ((length**2) - (length/2)**2)**0.5
        super().__init__(side=length, base=length, height=height)
    
    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()

class Rectangle(Quadrilateral):
    def __init__(self, base, height) -> None:
        super().__init__(base, height, side1=height, side2=height, top=base)
    
    def area(self):
        return super().area()

    def perimeter(self):
        return super().perimeter()

class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(base=length, height=length)

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return super().area()

