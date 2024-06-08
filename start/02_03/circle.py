"""
A class for representing a circle
"""


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def display_circumference(self) -> float:
        return 2 * 3.14 * self.radius

    def display_area(self) -> float:
        return 3.14 * self.radius * self.radius


circle1 = Circle(3)
print(circle1.display_area())
print(circle1.display_circumference())
