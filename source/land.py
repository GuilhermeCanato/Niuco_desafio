class Land:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.probe_positions = set()

    def inside_limits(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <=  self.height
    
    def check_position(self, x: int, y: int) -> bool:
        return (x, y) not in self.probe_positions

    def add_position(self, x: int, y: int):
        self.probe_positions.add((x, y))

    def free_position(self, x: int, y: int):
        self.probe_positions.discard((x, y))

    def __str__(self):
        return f"largura: {self.width}, altura: {self.height}"