class Polygon:
    def __init__(self) -> None:
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height) -> None:
        super().__init__()
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height / 2
    
    def perimeter(self):
        return super().perimeter()