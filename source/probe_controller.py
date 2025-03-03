from source.land import Land
from source.probe import Probe

from typing import List

class ProbeController:
    # Construtor da classe ProbeController
    def __init__(self, land: Land):
        self.land = land
        self.probes: List[Probe] = []

    # Função para adicionar uma nova sonda
    def add_probe(self, x: int, y: int, direction: str, commands: str):
        probe = Probe(x, y, direction, commands, self.land)
        self.probes.append(probe)

    # Função que decorre todas as sondas e executa o comando uma por vez
    def execute_probes(self):
        for probe in self.probes:
            probe.execute_comands()

    # Função com função apenas de log para mostrar as posições das sondas
    def show_probes_position(self):
        for probe in self.probes:
            print(probe)
    
    # Função que retorna os valores de todas as sonsas
    def show_probes_values(self):
        probes_values = []

        for probe in self.probes:
            probe_value = (probe.x, probe.y, probe.direction, probe.commands)
            probes_values.append(probe_value)

        return probes_values
