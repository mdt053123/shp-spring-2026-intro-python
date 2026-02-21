class Car:
    """
    Attributes: model, color, year
    """
    
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
        
    def __eq__(self, other):
        return self.model == other.model and self.color == other.color and self.year == other.year
    
    def __str__(self):
        return f"({self.model}, {self.color}, {self.year})"
    
maz = Car("mazda", "red", 1992)
maz_other = Car("mazda", "blue", 1992)
maz_duplicate = Car("mazda", "red", 1992)

print(maz)
print(maz_other)

print()

print(maz == maz_other)
print(maz == maz_duplicate)