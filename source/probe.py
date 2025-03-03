from source.land import Land

# Constante com as 4 direções possiveis
DIRECTIONS = ["N", "E", "S", "W"]

# Constante para indicar como a sonda vai se mover dependendo de cada direção. (Norte - Soma 1 no eixo Y, Lest - Soma 1 no eixo X, Sul - Substrai 1 do eixo Y e Oeste Substrai 1 do eixo X)
MOVEMENTS = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}

class Probe:
    # Construtor da classe Probe
    def __init__(self, x: int, y: int, direction: str, commands: str, land: Land):

        # Verifica antes de inicializar se a posição inicial ja está ocupada ou esta fora dos limites
        if not land.inside_limits(x, y) or not land.check_position(x, y):
            raise ValueError(f"Error: Posição inicial inválida, por que ja está ocupada por outra sonda ou está fora dos limites do planalto/terreno")

        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.land = land
        self.land.add_position(x, y)      

    # Função para virar 90° para a esquerda segue um ciclo circular N -> W -> S -> E -> N
    def turn_left(self):
        actual_direction = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(actual_direction - 1) % 4]

    # Função para virar 90° para a direita, segue um ciclo circular N -> E -> S -> W -> N
    def turn_right(self):
        actual_direction = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(actual_direction + 1) % 4]

    # Função para mover a sonda uma posição na direção dela
    def move(self):
        dx, dy = MOVEMENTS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy

        # Verifica se a posição está livre ou dentro dos limites do planalto, caso não estiver da uma mensagem de log de erro e ignora esse comando
        if self.land.inside_limits(new_x, new_y) and self.land.check_position(new_x, new_y):
            self.land.free_position(self.x, self.y)
            self.x, self.y = new_x, new_y
            self.land.add_position(self.x, self.y)
        else:
            print("ERROR: A sonda está fora do planalto ou a posição já está ocupada por outra sonda, ignorando comando!")

    # Função para direcionar cada letra do comando para executar uma determinada ação, caso não seja L, R ou M, apenas ignora a letra
    def execute_comands(self):
        for comand in self.commands:
            if comand == "L":
                self.turn_left()
            elif comand == "R":
                self.turn_right()
            elif comand == "M":
                self.move()
            else:
                print(f"Comando '{comand}' inválido, prosseguindo para o próximo comando!")
                pass
    
    # Override da função str() para a classe Probe
    def __str__(self):
        return f"x: {self.x}, y: {self.y}, direção: {self.direction}"