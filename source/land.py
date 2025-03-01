class Land:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def inside_limits(self, x: int, y: int):
        return 0 <= x <= self.width and 0 <= y <=  self.height

    def __str__(self):
        return f"largura: {self.width}, altura: {self.height}"