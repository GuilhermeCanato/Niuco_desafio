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
    def __init__(self, x: int, y: int, direction: str, land: Land):
        self.x = x
        self.y = y
        self.direction = direction
        self.land = land

    def turn_left(self):
        actual_direction = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(actual_direction - 1) % 4]

    def turn_right(self):
        actual_direction = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(actual_direction + 1) % 4]

    def move(self):
        dx, dy = MOVEMENTS[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy

        if self.land.inside_limits(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            print("ERROR: A sonda está fora do planalto, ignorando comando!")

    def execute_comands(self, comands: str):
        for comand in comands:
            if comand == "L":
                self.turn_left()
            elif comand == "R":
                self.turn_right()
            elif comand == "M":
                self.move()
            else:
                print(f"Comando '{comand}' não reconhecido, prosseguindo para o próximo comando!")
                pass

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, direção: {self.direction}"