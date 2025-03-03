class Land:
    # Construtor da classe Land
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.probe_positions = set()

    # Função para verificar se a entrada de um determinado x, y está dentro do limite do planalto/terreno
    def inside_limits(self, x: int, y: int) -> bool:
        return 0 <= x <= self.width and 0 <= y <=  self.height
    
    # Função para verificar se esta posição está livre
    def check_position(self, x: int, y: int) -> bool:
        return (x, y) not in self.probe_positions

    # Função para adicionar a posição de uma sonda
    def add_position(self, x: int, y: int):
        self.probe_positions.add((x, y))

    # Função para liberar uma posição de uma sonda
    def free_position(self, x: int, y: int):
        self.probe_positions.discard((x, y))

    # Override da função str() para a classe Land
    def __str__(self):
        return f"largura: {self.width}, altura: {self.height}"